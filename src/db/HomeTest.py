from beanie import Document, Indexed

class HomeTest(Document):
    request_id: Indexed(str, unique=True)
    access_time: str
    data: str


