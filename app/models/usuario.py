class Message():
    def __init__(self, message:str, author:str, destination:str, public:bool, id_author:int, id_destination:int, type_aut_dest:tuple) -> None:
        """
        Construtor de Message
        :param message -> mensagem
        :param author -> autor da mensagem
        :param destination -> quem recebe a mensagem
        :param public -> se a identidade do autor é pública ou não
        :param id_author -> identificador do author
        :param id_destination -> identificador do destinatario
        :param type_aut_dest -> tupla com o type do autor e destinatario
        """
        self.message = message
        self.author = author
        self.destination = destination
        self.upvotes = 0.0
        self.answers = []
        if public:
            self.link_author = f"/{type_aut_dest[0]}/" + str(id_author)
            self.link_receiver = f"/{type_aut_dest[1]}/" + str(id_destination)
        else:
            self.link_author = ""
            self.link_receiver = f"/{type_aut_dest[1]}/" + str(id_destination)

    def reply(self, answer) -> None:
        """
        Permite um usuário responder a uma mensagem
        :param answer -> resposta (Message)
        """
        self.answers.append(answer)

    def like(self) -> None:
        """
        Permite os usuarios darem like na mensagem, o que fará ela ganhar evidência
        """
        self.upvotes += 1

    def __lt__(self, __value) -> bool:
        return self.upvotes < __value.upvotes
    def __gt__(self, __value) -> bool:
        return self.upvotes > __value.upvotes  
    def __eq__(self, __value: object) -> bool:
        return self.upvotes == __value.upvotes  
    def __neq__(self, __value: object) -> bool:
        return self.upvotes == __value.upvotes  
    def __le__(self, __value) -> bool:
        return self.upvotes <= __value.upvotes
    def __ge__(self, __value) -> bool:
        return self.upvotes >= __value.upvotes


class Review(Message):
    def __init__(self, message: str, author: str, destination: str, public: bool, id_author: int, id_destination: int, type_aut_dest: tuple, rating: int) -> None:
        """
        Construtor de Review
        :param message -> mensagem
        :param author -> autor da mensagem
        :param destination -> quem recebe a mensagem
        :param public -> se a identidade do autor é pública ou não
        :param id_author -> identificador do author
        :param id_destination -> identificador do destinatario
        :param type_aut_dest -> tupla com o type do autor e destinatario
        :param rating -> nota da avaliação
        """
        super().__init__(message, author, destination, public, id_author, id_destination, type_aut_dest)
        self.rating = rating


class User():
    def __init__(self, name: str, last_name: str, age: int, classes: list) -> None:
        """
        Construtor de Usuario
        :param name -> nome do usuario
        :param last_name -> sobrenome do usuario
        :param age -> idade do usuario
        :param classes -> lista com as materias cursadas/ministradas pelo usuário
        """
        self.data = dict()
        self.name = name
        self.last_name = last_name
        self.data["age"] = age
        self.data["classes"] = classes


class Student(User):
    def __init__(self, name: str, last_name: str, age: int, classes: list, teachers: list, curso: str, periodo: int, matricula: int) -> None:
        """
        Construtor de Aluno
        :param curso -> o curso do aluno
        :param periodo -> periodo que ele se encontra
        :param matricula -> matricula do aluno
        """
        super().__init__(name, last_name, age, classes)
        self.data["curso"] = curso
        self.data["periodo"] = periodo
        self.id = matricula
        self.teachers = teachers
        self.available_reviews = teachers.copy()

    """    
    def mostra_perfil(self, public: bool) -> tuple:
    ""
    Retorna as informações do perfil de acordo com a opção de privacidade definida pelo usuário
    :param public -> True se for publica sua identidade, False se desejar anonimato
    ""
    if public:
        return self.name, self.last_name, self.age, self.classes, self.data
    else: 
        return "Student", str(self.id), 15, [], {}
    """

    def write_review(self, subject: str, teacher: str, teacher_id:int, message: str, rating: int, public: bool = True) -> Review:
        """
        Aluno escreve uma Review para um professor específico
        :param subject -> materia a qual se refere a avaliação
        :param teacher -> nome do professor avaliado
        :param teacher_id -> id do professor
        :param message -> mensagem da review
        :param rating -> nota dada ao professor
        :param public -> se a identidade do avaliador estará pública
        :return -> Review
        """
        if subject in self.data["classes"] and teacher in self.available_reviews:
            self.available_reviews.remove(teacher)
            nome = self.name + self.last_name
            return Review(message, nome, teacher, public, self.id, teacher_id, ("aluno", "professor"), rating)

class Teacher(User):
    ID = 1

    def __init__(self, name: str, last_name: str, age: int, classes: list, departamento: str) -> None:
        """
        Construtor de Professor
        :param name -> nome do professor
        :param last_name -> sobrenome do professor
        :param age -> idade do professor
        :param classes -> lista com as materias ministradas pelo usuário
        :param departamento -> departamento que o professor pertence
        """     
        super().__init__(name, last_name, age, classes)
        self.data["departamento"] = departamento
        self.ratings = []
        self.avarege_rating = 0.0
        self.reviews = []
        self.id = Teacher.ID
        Teacher.ID += 1

    def recive_review(self, review: Review) -> None:
        """
        Adiciona uma nova review às avaliações do professor
        :param review -> avaliação do professor
        """
        self.ratings.append(review.rating)
        self.reviews.append(review)
        self.avarege_rating = self.calculate_avarege_rating()

    def calculate_avarege_rating(self) -> float:
        size = len(self.ratings)
        return sum(self.ratings)/size