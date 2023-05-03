from quart import Quart, request, render_template, make_response, redirect, url_for
from beanie import init_beanie
from src.db.Session import Session
from src.db.User import User
from src.db.parse_login import create_mongodb_uri
from motor.motor_asyncio import AsyncIOMotorClient
import dotenv
import os

app = Quart("review_professores", template_folder="src/templates")

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

@app.route("/")
async def index():
   message = request.cookies.get("index_message")
   if message is None:
      return await render_template("index.html")
   else:
      response = await make_response(await render_template("index.html", message=message))
      response.delete_cookie("index_message")
      return response

@app.route("/login", methods=['GET', 'POST'])
async def login():
   if request.method == "POST":
      username = (await request.form)['username'].strip()
      password_hash = (await request.form)['password_hash']
      user = await User.find({"safe_username": username.lower()}).first_or_none()
      if user is not None:
         if user.password_hash == password_hash:
            new_session = await Session.create_session(user)
            response = await make_response(redirect(url_for("index")))
            response.set_cookie("current_session", new_session.session_id)
            response.set_cookie("index_message", "Logado com sucesso!")
            return response

      return await render_template("login.html", message="Credenciais incorretas.")
   else:
      session = await Session.find({"session_id": request.cookies.get("current_session")}).first_or_none()
      if session is not None:
         if not (await session.is_expired()):
            await session.renew()
            response = await make_response(redirect(url_for("index")))
            response.set_cookie("index_message", "Você já está logado!")
            return response

      return await render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
async def register():
   if request.method == "POST":
      username: str = (await request.form)['username'].strip()
      password_hash = (await request.form)['password_hash']

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

@app.route("/logout", methods=['GET'])
async def logout():
   session = await Session.find({"session_id": request.cookies.get("current_session")}).first_or_none()
   if session is None:
      return redirect(url_for("index"))
   else:
      await session.delete_session()
      response = await make_response(redirect(url_for("index")))
      response.set_cookie("index_message", "Desconectado com sucesso.")
      return response

app.run()
