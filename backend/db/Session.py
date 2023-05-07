from typing import Union
from uuid import uuid4
from beanie import Document, Indexed
from datetime import datetime, timedelta
from db.User import User

DAYS_TO_EXPIRE = 60


class Session(Document):
    """
    Representa uma sessão de login. O id da sessão deve ser passado
    como cookie para o navegador sempre que aplicável.
    """

    session_id: Indexed(str, unique=True)
    expire_date: str
    linked_user_id: str

    async def is_expired(self) -> Union[User, bool]:
        """
        Verifica se a sessão está expirada. Se estiver expirada deleta a sessão do banco de dados.
        :return: True se estiver expirada e False caso contrário.
        """
        datetime_obj = datetime.fromisoformat(self.expire_date)
        if datetime.utcnow() - datetime_obj > timedelta(days=DAYS_TO_EXPIRE):
            await self.delete_session()
            return True
        return False

    async def renew(self):
        """
        Renova a sessão.
        :return: None
        """
        new_expire_date = datetime.utcnow() + timedelta(days=DAYS_TO_EXPIRE)
        self.expire_date = new_expire_date.isoformat()
        await self.save()

    async def delete_session(self):
        """
        Deleta a sessão do banco de dados.
        :return: None
        """
        await self.delete()
        linked_user = await User.find({"user_id": self.linked_user_id}).first_or_none()
        if linked_user is not None:
            linked_user.sessions.remove(self.session_id)
            await linked_user.save()

    @classmethod
    async def create_session(cls, user: User):
        """
        Cria uma sessão nova para um usuário.
        :param user: O usuário para qual a sessão vai ser criada.
        :return: A nova sessão.
        """
        new_id = str(uuid4())
        user.sessions.append(new_id)
        await user.save()

        new_session = cls(session_id=new_id, expire_date="", linked_user_id=user.user_id)
        await new_session.renew()
        return new_session
