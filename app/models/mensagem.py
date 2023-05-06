from datetime import datetime

class Message():
    def __init__(self, message:str, public:bool, id_author:int, id_destination:int, data: datetime) -> None:
        """
        Construtor de Message
        :param message -> mensagem
        :param author -> autor da mensagem
        :param destination -> quem recebe a mensagem
        :param public -> se a identidade do autor é pública ou não
        :param id_author -> identificador do author
        :param id_destination -> identificador do destinatario
        :param  -> tupla com o type do autor e destinatario
        """
        self.message = message
        self.destination = id_destination
        self.data = data
        self.upvotes = 0.0
        self.answers = []
        self.likes = []
        self.author = "Anonimo"
        if public:
            self.author = id_author

    def reply(self, answer) -> None:
        """
        Permite um usuário responder a uma mensagem
        :param answer -> resposta (Message)
        """
        self.answers.append(answer)

    def like(self, author_id) -> None:
        """
        Permite os usuarios darem like na mensagem, o que fará ela ganhar evidência
        :param author_id -> identidade de quem curtiu
        """
        if author_id not in self.likes:
            self.likes.append(author_id)
            self.upvotes += 1

    def unlike(self, author_id) -> None:
        """
        Permite o usuário deixar de curtir
        :param author_id -> identidade de quem curtiu
        """
        if author_id in self.likes:
            self.likes.remove(author_id)
            self.upvotes -= 1

class Review(Message):
    def __init__(self, message: str, public: bool, id_author: int, id_destination: int, data: datetime, rating: int) -> None:
        """
        Construtor de Review
        :param message -> mensagem
        :param author -> autor da mensagem
        :param destination -> quem recebe a mensagem
        :param public -> se a identidade do autor é pública ou não
        :param id_author -> identificador do author
        :param id_destination -> identificador do destinatario
        :param  -> 
        :param rating -> nota da avaliação
        """
        super().__init__(message, public, id_author, id_destination, data)
        self.rating = rating