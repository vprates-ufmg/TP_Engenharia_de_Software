from dataclasses import asdict

from quart import Quart, request, render_template, make_response, redirect, url_for, jsonify
from beanie import init_beanie

from api_responses import UserData, UserResponse, GenericResponse
from db.Session import Session
from db.User import User
from db.parse_login import create_mongodb_uri
from motor.motor_asyncio import AsyncIOMotorClient
import dotenv
import os

app = Quart("review_professores", template_folder="src/templates", static_folder="src/static")


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
async def login():
    """
    Verifica as credenciais enviadas e faz login.
    Esse endpoint deve receber um application/json com os campos "username" e "password_hash"
    Retorna um LoginResponse com o objeto UserResponse caso as credenciais baterem. Retorna 401 caso contrário.
    """
    if request.method == "POST":
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
                user = UserData(user.user_id, user.username, new_session.session_id)
                response = UserResponse(True, "", user)
                return asdict(response), 200

        return asdict(UserResponse(False, "Credenciais incorretas.", None)), 401


@app.route("/register", methods=["GET", "POST"])
async def register():
    """
    Registra o usuário no sistema. Caso já existir um usuário de mesmo nome, retorna erro. Se já estiver logado, redireciona para o index.html.
    :return: renderiza o template do register.html
    """
    if request.method == "POST":
        username: str = (await request.form)["username"].strip()
        if username == "":
            return await render_template("register.html", message="Nome de usuário não pode ser vazio.")

        password_hash = (await request.form)["password_hash"]

        user = await User.find({"safe_username": username.lower()}).first_or_none()
        if user is not None:
            return await render_template("register.html", message="Nome de usuário não disponível.")

        await User.create_user(username, password_hash)
        return await render_template("login.html", message="Conta criada com sucesso. Você pode entrar.")

    else:
        session = await Session.find({"session_id": request.cookies.get("current_session")}).first_or_none()
        if session is not None:
            if not (await session.is_expired()):
                await session.renew()
                response = await make_response(redirect(url_for("index")))
                response.set_cookie("index_message", "Você já está logado!")
                return response

        return await render_template("register.html")


@app.route("/logout", methods=["GET"])
async def logout():
    """
    Desconecta o usuário do sistema, deletando a sessão salva.
    :return: redireciona para o index.html após desconexão
    """
    session = await Session.find({"session_id": request.cookies.get("current_session")}).first_or_none()
    if session is None:
        return redirect(url_for("index"))
    else:
        await session.delete_session()
        response = await make_response(redirect(url_for("index")))
        response.set_cookie("index_message", "Desconectado com sucesso.")
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run()
