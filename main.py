from quart import Quart
from beanie import init_beanie
from src.db.HomeTest import HomeTest
from src.db.parse_login import create_mongodb_uri
from motor.motor_asyncio import AsyncIOMotorClient
import dotenv
import os

app = Quart("review_professores")

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
   await init_beanie(getattr(client, mongodb_database), document_models=[HomeTest])

@app.route("/")
async def hello_world():
    n_entries = len(await HomeTest.find({}).to_list())
    return f"<p>Hello, World! There are {n_entries} entries in the database.</p>"

app.run()
