from quart import Quart

app = Quart(__name__)

from app.controllers import default