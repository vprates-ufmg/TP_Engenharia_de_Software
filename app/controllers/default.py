from quart import render_template
from run import app
from app.models.usuario import *

aluno = Student("Joao Messi", ["PDS1", "OC1", "ALC"], ["Ronaldinho Gaucho", "Cristiano Ronaldo", "Ronaldo Fenomeno"], 
        "Engenharia de Software", 6, 2030009563)

def lista_com_todos_os_profs_e_ids():
    """
    Retorna a lista de tuplas de todos os profs e suas ids distintos do banco de dados
    retorna: tuplas de listas (nome prof, id)
    """
    db = [] # fingindo q db é o banco de dados
    nomes = []
    ids = []
    for prof in db:
        nomes.append(prof["nome"])
        ids.append(prof["id"])
    return nomes, ids

def coleta_reviews_professor(prof, sort = "data"):
    """
    retorna todas as reviews do professor X
    """
    db = [] # simulando o DB via lista
    mensagens = []
    for db_linha in db:
        if db_linha["id"] == prof:
            nome = db_linha["nome"]
            mensagens = db_linha["mensagens"] #considerando que estão todas salvas em uma mesma lista
            break
    if sort == "data":
        return nome, sorted(mensagens, key = mensagens["data"]) # considerando que elas tem o formato parecido ao da classe
    elif sort == "upvotes":
        return nome, sorted(mensagens, key = mensagens["upvotes"])
    else:
        return nome, mensagens    

@app.route("/prof")
async def list_teachers():
    """
    Retorna uma lista com todos os professores cadastrados
    ao clicar em um é possível acessar sua página
    """
    nomes, ids = lista_com_todos_os_profs_e_ids()
    return await render_template('profs.html', profs = nomes, ids = ids)


@app.route("/prof/<id>")
async def retorna_re(id):
    if id.isnumeric():
        if id in list:
            id = int(id)
            nome, list = coleta_reviews_professor(id)
            return await render_template('professor.html', nome = nome, id = id, mensagens = list)
    return app.redirect("/prof")