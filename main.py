from quart import Quart, request, render_template, make_response
from beanie import init_beanie
from src.db.HomeTest import HomeTest
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
   await init_beanie(getattr(client, mongodb_database), document_models=[HomeTest, User, Session])

@app.route("/")
async def hello_world():
    n_entries = len(await HomeTest.find({}).to_list())
    return f"<p>Hello, World! There are {n_entries} entries in the database.</p>"

@app.route("/login", methods=['GET', 'POST'])
async def login():
   if request.method == "POST":
      username = (await request.form)['username']
      password_hash = (await request.form)['password_hash']
      user = await User.find({"username": username}).first_or_none()
      if user is not None:
         if user.password_hash == password_hash:
            new_session = await Session.create_session(user)
            response = await make_response(render_template("index.html", message="Logado com sucesso!"))
            response.set_cookie("current_session", new_session.session_id)
            return response

      return await render_template("login.html", message="Credenciais incorretas.")
   else:
      session = await Session.find({"session_id": request.cookies.get("current_session")}).first_or_none()
      if session is not None:
         if not (await session.is_expired()):
            await session.renew()
            return await render_template("index.html", message="Você já está logado!")

      return await render_template("login.html")

app.run()
