"""
Módulo que importa os dados da planilha para o banco de dados
"""
import pandas as pd
from pymongo import MongoClient
from bson.son import SON

import settings


def connect_database() -> MongoClient:
    """
    Função que realia a conexão com o banco de dados
    :return: conexão com o banco
    """
    print("Conectando-se com o banco de dados...", end="")

    client = MongoClient(settings.Config().MONGO_URI)
    db = client["database1"]

    print("OK")
    return db


def read_csv(file: str) -> pd.DataFrame:
    """
    Função que realiza a leitura do arquivo csv
    :param file: Nome do arquivo
    :return: DataFrame com os dados do arquivo
    """
    print("Realizando a leitura dos dados do arquivo...", end="")

    # Lendo arquivo csv
    df = pd.read_csv(
        file,
        delimiter=",",
        encoding="Utf-8",
        dtype={
            "nome": str,
            "idade_ate_31_12_2016": float,
            "ra": float,
            "campus": str,
            "municipio": str,
            "curso": str,
            "modalidade": str,
            "nivel_do_curso": str,
            "data_inicio": str,
        },
        parse_dates=["data_inicio"],
    )

    # Substituindo NaN por None
    df.where(df.notnull(), None)

    # Retirando espaços no começo e fim das strings
    df["nome"] = df["nome"].str.strip()
    df["campus"] = df["campus"].str.strip()
    df["municipio"] = df["municipio"].str.strip()
    df["curso"] = df["curso"].str.strip()
    df["modalidade"] = df["modalidade"].str.strip()
    df["nivel_do_curso"] = df["nivel_do_curso"].str.strip()

    print("OK")
    return df


def create_collection_students(df: pd.DataFrame, db: MongoClient) -> None:
    """
    Função que cria e popula a collection students
    :param df: dataset
    :param db: banco de dados
    """
    print("Formatando dados...", end="")

    # Recriando a collection students
    collection_students = db["students"]
    collection_students.drop()
    collection_students = db["students"]

    # Filtrando dados de alunos e retirando duplicatas
    students = df[["nome", "idade_ate_31_12_2016", "ra"]]
    students = students.drop_duplicates()

    # Criando lista de alunos
    students_list = []

    for student in students.values:
        students_list.append(
            {
                "name": student[0],
                "age": student[1],
                "ra": student[2],
                "courses": []
            }
        )

    # Filtrando cursos de alunos
    courses = df[[
        "nome",
        "campus",
        "municipio",
        "curso",
        "modalidade",
        "nivel_do_curso",
        "data_inicio",
    ]]

    # Criando lista de cursos
    courses_list = []

    for course in courses.values:
        courses_list.append(
            {
                "name": course[0],
                "campus": course[1],
                "county": course[2],
                "course": course[3],
                "modality": course[4],
                "level": course[5],
                "start_date": course[6],
            }
        )

    # Inserindo cursos na lista de alunos
    for course in courses_list:
        for student in students_list:
            if course["name"] == student["name"]:
                student["courses"].append(
                    SON([
                        ("campus", course["campus"]),
                        ("county", course["county"]),
                        ("course", course["course"]),
                        ("modality", course["modality"]),
                        ("level", course["level"]),
                        ("start_date", course["start_date"]),
                    ])
                )

    print("OK")
    print("Inserindo dados no banco de dados...", end="")

    # Inserindo dados formatados na collection students
    collection_students.insert_many(students_list)

    print("OK")


if __name__ == "__main__":
    # Polando banco de dados
    mongo = connect_database()
    dataset = read_csv("dataset_estudantes.csv")
    create_collection_students(dataset, mongo)
