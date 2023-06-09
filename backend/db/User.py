from typing import List
from uuid import uuid4
from beanie import Document, Indexed


class User(Document):
    """
    Representa um usuário da plataforma do site.
    """

    user_id: Indexed(str, unique=True)
    username: str
    safe_username: str
    password_hash: str
    sessions: List[str]
    upvoted_reviews: list = []
    downvoted_reviews: list = []

    @classmethod
    async def create_user(cls, username: str, password_hash: str):
        """
        Cria um usuário no banco de dados.
        :param username: o nome de usuário do usuário
        :param password_hash: o hash da senha do usuário
        :return: o usuário novo
        """
        new_id = str(uuid4())
        new_user = cls(
            user_id=new_id, username=username, safe_username=username.lower(), password_hash=password_hash, sessions=[]
        )
        await new_user.save()
        return new_user
