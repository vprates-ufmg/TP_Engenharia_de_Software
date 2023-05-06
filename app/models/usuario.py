from app.models.mensagem import Message, Review

class User():
    def __init__(self, name: str, classes: list) -> None:
        """
        Construtor de Usuario
        :param name -> nome do usuario
        :param last_name -> sobrenome do usuario
        :param age -> idade do usuario
        :param classes -> lista com as materias cursadas/ministradas pelo usuário
        """
        self.name = name
        self.classes = classes

class Student(User):
    def __init__(self, name: str, classes: list, teachers: list, curso: str, periodo: int, matricula: int) -> None:
        """
        Construtor de Aluno
        :param teachers -> lista de professores
        :param curso -> o curso do aluno
        :param periodo -> periodo que ele se encontra
        :param matricula -> matricula do aluno
        """
        super().__init__(name, classes)
        self.curso = curso
        self.periodo = periodo
        self.id = matricula
        self.teachers = teachers
        self.available_reviews = teachers.copy()

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
        if subject in self.classes and teacher in self.available_reviews:
            self.available_reviews.remove(teacher) # garante que não haverá mais de uma review de um aluno para o mesmo professor
            return Review(message, self.nome, teacher, public, self.id, teacher_id, ("aluno", "professor"), rating)

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
        super().__init__(name, classes)
        self.departamento = departamento
        self.avarege_rating = 0.0
        self.ratings = []
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