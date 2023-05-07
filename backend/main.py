from dataclasses import asdict
from quart import Quart, request, jsonify
from beanie import init_beanie
from quart_cors import cors, route_cors
from quart_rate_limiter import RateLimiter, rate_exempt
from api_responses import UserData, UserResponse, GenericResponse, ReviewData, ReviewResponse
from db.Review import SortingMethod, Review
from db.Session import Session
from db.User import User
from db.Disciplina import Disciplina
from db.Turma import Turma
from db.Professor import Professor
from db.parse_login import create_mongodb_uri
from motor.motor_asyncio import AsyncIOMotorClient
import dotenv
import os

app = Quart("review_professores")
app = cors(app, allow_origin="*")
rate_limiter = RateLimiter(app)


@app.before_serving
async def init_database():
    dotenv.load_dotenv()
    mongodb_server = os.getenv("MONGODB_SERVER")
    mongodb_port = os.getenv("MONGODB_PORT")
    mongodb_username = os.getenv("MONGODB_USERNAME")
    mongodb_password = os.getenv("MONGODB_PASSWORD")
    mongodb_auth_db = os.getenv("MONGODB_AUTH_DB")
    mongodb_database = os.getenv("MONGODB_DATABASE")

    uri = create_mongodb_uri(mongodb_server, mongodb_port, mongodb_username, mongodb_password, mongodb_auth_db)
    client = AsyncIOMotorClient(uri)
    await init_beanie(
        getattr(client, mongodb_database), document_models=[User, Session, Review, Disciplina, Turma, Professor]
    )


def bad_request():
    return asdict(GenericResponse(False, "Bad Request")), 400


@app.route("/login", methods=["POST"])
# @rate_limit(5, timedelta(minutes=1)) # descomentar e comentar o abaixo antes do merge
@rate_exempt
@route_cors(allow_origin="*")
async def login():
    """
    Verifica as credenciais enviadas e faz login.
    Esse endpoint deve receber um application/json com os campos "username" e "password_hash"
    Retorna um LoginResponse com o objeto UserResponse caso as credenciais baterem.
    Retorna 401 caso contrário.
    Retorna 409 caso o usuário já estiver logado.
    """
    session = await Session.find({"session_id": request.cookies.get("current_session")}).first_or_none()
    if session is not None:
        user = await User.find({"user_id": session.linked_user_id}).first_or_none()
        if not (await session.is_expired()):
            await session.renew()
            user = UserData(user.user_id, user.username)
            return asdict(UserResponse(False, "Você já está logado!", user)), 409

    data = await request.json
    if data is None:
        return bad_request()

    username = data.get("username", "").strip()
    password_hash = data.get("password_hash", "")

    if not username or not password_hash:
        return bad_request()

    user = await User.find({"safe_username": username.lower()}).first_or_none()
    if user is not None:
        if user.password_hash == password_hash:
            new_session = await Session.create_session(user)
            user = UserData(user.user_id, user.username)
            response = UserResponse(True, "Logado com sucesso.", user)
            out = jsonify(asdict(response))
            out.set_cookie("current_session", new_session.session_id)
            return out, 200

    return asdict(UserResponse(False, "Credenciais incorretas.", None)), 401


@app.route("/register", methods=["POST"])
# @rate_limit(3, timedelta(minutes=1)) # descomentar e comentar o abaixo antes do merge
@rate_exempt
@route_cors(allow_origin="*")
async def register():
    """
    Registra o usuário no sistema.
    Caso já existir um usuário de mesmo nome, retorna 409.
    Caso os requisitos de senha e username não forem cumpridos, retorna 400.
    """
    session = await Session.find({"session_id": request.cookies.get("current_session")}).first_or_none()
    if session is not None:
        user = await User.find({"user_id": session.linked_user_id}).first_or_none()
        if not (await session.is_expired()):
            await session.renew()
            user = UserData(user.user_id, user.username)
            return asdict(UserResponse(False, "Você já está logado!", user)), 409

    data = await request.json
    if data is None:
        return bad_request()

    username = data.get("username", "").strip()
    password_hash = data.get("password_hash", "")

    if not username or not password_hash:
        return bad_request()

    user = await User.find({"safe_username": username.lower()}).first_or_none()
    if user is not None:
        return asdict(UserResponse(False, "Já existe um usuário com esse nome.", None)), 409

    user_db = await User.create_user(username, password_hash)
    new_session = await Session.create_session(user_db)
    user = UserData(user_db.user_id, user_db.username)
    response = UserResponse(True, "Conta registrada com sucesso.", user)
    out = jsonify(asdict(response))
    out.set_cookie("current_session", new_session.session_id)
    return out, 200


@app.route("/logout", methods=["GET"])
@rate_exempt
@route_cors(allow_origin="*")
async def logout():
    """
    Desconecta o usuário do sistema, deletando a sessão salva.
    Esse endpoint sempre retorna 200.
    """
    session = await Session.find({"session_id": request.cookies.get("current_session")}).first_or_none()
    if session is None:
        return asdict(GenericResponse(True, "Já desconectado.")), 200
    else:
        await session.delete_session()
        response = GenericResponse(True, "Desconectado com sucesso.")
        out = jsonify(asdict(response))
        out.delete_cookie("current_session")
        return out, 200


@app.route("/create_review", methods=["POST"])
# @rate_limit(10, timedelta(minutes=1)) # descomentar e comentar o abaixo antes do merge
@rate_exempt
@route_cors(allow_origin="*")
async def create_review():
    """
    Cria uma review no site. O cookie "session_id" deve estar setado, indicando que o usuário está logado.
    O json de requisição deve ser algo do tipo:
    {
        "semester": "2021/2",
        "teacher_id": "120526b0-9a0a-498c-acae-8d25a98d03e1",
        "disciplina_id": "f0fc331b-1bb7-4978-91c6-ffff45141658",
        "is_anonymous": false,
        "content": "muito bom o professor, mas no maximo 500 caracteres"
    }
    Retorna 403 se não estiver logado.
    Retorna 404 se a disciplina ou o professor não forem encontrados.
    Retorna 413 se a mensagem for grande demais.
    """
    session = await Session.find({"session_id": request.cookies.get("current_session")}).first_or_none()
    if session is None:
        return asdict(GenericResponse(False, "Você não está logado!")), 403
    else:
        if await session.is_expired():
            return asdict(GenericResponse(False, "Por favor, faça login novamente.")), 403

    user = await User.find(User.user_id == session.linked_user_id).first_or_none()
    if user is None:
        await session.delete_session()
        out = jsonify(asdict(GenericResponse(False, "Conta inexistente.")))
        out.delete_cookie("current_session")
        return out, 403

    data = await request.json
    if data is None:
        return bad_request()

    semester = data.get("semester", "")
    teacher = data.get("teacher_id", "")
    disciplina = data.get("disciplina_id", "")
    content = data.get("content", "")
    is_anonymous = data.get("is_anonymous", "")
    if not semester or not teacher or not disciplina or not content or is_anonymous == "":
        return bad_request()

    if len(content) > 500:
        return asdict(GenericResponse(False, "Mensagem grande demais.")), 413

    teacher = await Professor.find(Professor.uid_professor == teacher).first_or_none()
    if teacher is None:
        return asdict(GenericResponse(False, "Professor inexistente.")), 404

    disciplina = await Disciplina.find(Disciplina.id_disciplina == disciplina).first_or_none()
    if disciplina is None:
        return asdict(GenericResponse(False, "Disciplina inexistente.")), 404

    turma = await Turma.find(
        Turma.id_disciplina == disciplina.id_disciplina,
        Turma.uid_professor_ministrante == teacher.uid_professor,
        Turma.semestre == semester,
    ).first_or_none()
    if turma is None:
        return asdict(GenericResponse(False, "Esse professor não ministrou essa matéria nesse semestre.")), 404

    review_obj = await Review.create_review(
        user.username, user.user_id, is_anonymous, teacher.uid_professor, disciplina.id_disciplina, semester, content
    )

    user.upvoted_reviews.append(review_obj.id_review)
    await user.save()

    review = ReviewData(
        autor="Anônimo" if review_obj.is_anonymous else review_obj.author,
        content=review_obj.content,
        time=review_obj.time,
        votes=review_obj.n_votes,
        semester=semester,
        professor=teacher.nome,
        disciplina=disciplina.nome,
    )
    return asdict(ReviewResponse(True, "Review criado com sucesso!", [review])), 200


@app.route("/fetch_review", methods=["GET"])
# @rate_limit(10, timedelta(minutes=1)) # descomentar e comentar o abaixo antes do merge
@rate_exempt
@route_cors(allow_origin="*")
async def fetch_review():
    """
    Obtêm uma lista de reviews que se encaixam nos filtros.
    O json de requisição deve ser algo do tipo:
    {
        "sorting": 0,
        "semester": "2020/2"
        "teacher_id": "120526b0-9a0a-498c-acae-8d25a98d03e1",
        "disciplina_id": "f0fc331b-1bb7-4978-91c6-ffff45141658",
        "range_start": 0,
        "range_end": 15
    }
    sorting simboliza o Enum SortingMethod
    semester, teacher_id e disciplina_id, range_start e range_end são opcionais
    range_start é 0 por padrão, e range_end é 15 por padrão.
    Retorna 400 se não possuir o "sorting"
    """
    data = await request.json
    if data is None:
        return bad_request()

    sorting_method = data.get("sorting", "")
    if sorting_method not in [
        SortingMethod.NEWEST_FIRST,
        SortingMethod.OLDEST_FIRST,
        SortingMethod.MOST_UPVOTED,
        SortingMethod.LEAST_UPVOTED,
    ]:
        return bad_request()

    range_start = data.get("range_start", 0)
    range_end = data.get("range_end", 15)
    try:
        range_start = int(range_start)
        range_end = int(range_end)
    except ValueError:
        return bad_request()

    mongodb_query = {}
    semester = data.get("semester", "")
    if semester:
        mongodb_query["semester"] = semester

    teacher = data.get("teacher_id", "")
    if teacher:
        mongodb_query["teacher_id"] = teacher

    disciplina = data.get("disciplina_id", "")
    if disciplina:
        mongodb_query["disciplina_id"] = disciplina

    sort = ()
    if sorting_method == SortingMethod.NEWEST_FIRST:
        sort = ("-time", "-n_votes")
    elif sorting_method == SortingMethod.OLDEST_FIRST:
        sort = ("+time", "-n_votes")
    elif sorting_method == SortingMethod.MOST_UPVOTED:
        sort = ("-n_votes", "-time")
    elif sorting_method == SortingMethod.LEAST_UPVOTED:
        sort = ("+n_votes", "-time")

    eligible = await Review.find(mongodb_query).skip(range_start).limit(range_end - range_start).sort(*sort).to_list()

    response_data = []
    for result in eligible:
        disciplina = await Disciplina.find(Disciplina.id_disciplina == result.disciplina_id).first_or_none()
        professor = await Professor.find(Professor.uid_professor == result.teacher_id).first_or_none()
        if not disciplina or not professor:
            continue

        response_data.append(
            ReviewData(
                autor="Anônimo" if result.is_anonymous else result.author,
                content=result.content,
                time=result.time,
                votes=result.n_votes,
                semester=result.semester,
                professor=professor.nome,
                disciplina=disciplina.nome,
            )
        )

    return asdict(ReviewResponse(True, "Dados obtidos com sucesso!", response_data)), 200


if __name__ == "__main__":
    app.run()
