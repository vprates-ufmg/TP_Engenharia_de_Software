from typing import List
from uuid import uuid4

from beanie import Document, Indexed

class User(Document):
    user_id: Indexed(str, unique=True)
    username: str
    safe_username: str
    password_hash: str
    sessions: List[str]

    @classmethod
    async def create_user(cls, username: str, password_hash: str):
        new_id = str(uuid4())
        new_user = cls(user_id=new_id, username=username, safe_username=username.lower(), password_hash=password_hash, sessions=[])
        await new_user.save()
        return new_user