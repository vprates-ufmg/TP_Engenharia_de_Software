"""
Arquivo responsável por ler do arquivo .csv providenciado,
os dados dos professores, matérias e semestres em que as matérias
foram ofertadas.
Deve ser um .csv com as colunas ["sem", "cod", "mat", "prof"].
"""
import asyncio
import os
from uuid import uuid4
import dotenv
import pandas as pd
import sys
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from Disciplina import Disciplina
from Professor import Professor
from Turma import Turma
from parse_login import create_mongodb_uri

try:
    file_path = sys.argv[1]
except IndexError:
    print(f"usage: python3 {sys.argv[0]} filepath.csv")
    exit(1)

df = pd.read_csv(file_path, sep="$")


async def init_database():
    dotenv.load_dotenv()
    mongodb_server = os.getenv("MONGODB_SERVER")
    mongodb_port = os.getenv("MONGODB_PORT")
    mongodb_username = os.getenv("MONGODB_USERNAME")
    mongodb_password = os.getenv("MONGODB_PASSWORD")
    mongodb_database = os.getenv("MONGODB_DATABASE")

    uri = create_mongodb_uri(mongodb_server, mongodb_port, mongodb_username, mongodb_password)
    client = AsyncIOMotorClient(uri)
    await init_beanie(getattr(client, mongodb_database), document_models=[Professor, Turma, Disciplina])


async def main():
    await init_database()

    for teacher in df["prof"].unique():
        exists = await Professor.find({"nome": teacher}).first_or_none()
        if not exists:
            new = Professor(uid_professor=str(uuid4()), nome=teacher)
            await new.save()

    for disc_cod, disc_nome in zip(df["cod"], df["mat"]):
        exists = await Disciplina.find({"nome": disc_nome.strip()}).first_or_none()
        if not exists:
            new = Disciplina(id_disciplina=str(uuid4()), cod_disciplina=disc_cod.strip(), nome=disc_nome.strip())
            await new.save()

    for sem, mat, prof in zip(df["sem"], df["mat"], df["prof"]):
        prof = await Professor.find({"nome": prof}).first_or_none()
        mat = await Disciplina.find({"nome": mat.strip()}).first_or_none()
        new = Turma(
            cod_disciplina=mat.cod_disciplina,
            semestre=sem.strip(),
            id_disciplina=mat.id_disciplina,
            uid_professor_ministrante=prof.uid_professor,
        )
        await new.save()


asyncio.run(main())
