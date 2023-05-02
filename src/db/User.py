from typing import List

from beanie import Document, Indexed

class User(Document):
    user_id: Indexed(str, unique=True)
    username: str
    password_hash: str
    sessions: List[str]