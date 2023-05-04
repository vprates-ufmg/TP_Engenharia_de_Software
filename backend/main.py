from dataclasses import asdict
from datetime import timedelta

from quart import Quart, request, jsonify
from beanie import init_beanie
from quart_rate_limiter import RateLimiter, rate_limit, rate_exempt
from api_responses import UserData, UserResponse, GenericResponse
from db.Session import Session
from db.User import User
from db.parse_login import create_mongodb_uri
from motor.motor_asyncio import AsyncIOMotorClient
import dotenv
import os

app = Quart("review_professores")
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
    await init_beanie(getattr(client, mongodb_database), document_models=[User, Session])


def bad_request():
    return asdict(GenericResponse(False, "Bad Request")), 400


@app.route("/login", methods=["POST"])
@rate_limit(5, timedelta(minutes=1))
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
@rate_limit(3, timedelta(minutes=1))
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

    if len(username) < 4:
        return asdict(GenericResponse(False, "O nome de usuário deve conter no mínimo 4 caracteres.")), 400

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


if __name__ == "__main__":
    app.run()
