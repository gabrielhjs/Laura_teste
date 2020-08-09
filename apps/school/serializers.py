"""
Módulo de serialização dos dados do aplicativo school
"""
from datetime import datetime
from wtforms import Form
from pymongo import ReturnDocument
from bson.json_util import dumps

from extensions import mongo, cache


def student_get(ra: int) -> dumps:
    """
    Serializer que busca por estudante
    :param ra: RA do aluno desejado
    :return: json
    """
    collection_students = mongo.db.students

    # Buscando por cache
    cached_data = cache.get("student_get" + str(ra))

    # Verificando se existe cache
    if cached_data is not None:
        return dumps(cached_data)

    query = collection_students.find_one(
        {
            "ra": ra,
        }
    )

    # Armazenando dados atualizados no cache
    cache.set("student_get" + str(ra), query)

    return dumps(query)


def student_post(form: Form) -> dumps:
    """
    Serializer que cadastra ou atualiza dados de estudantes
    :return: json
    """
    collection_students = mongo.db.students

    query = collection_students.find_one_and_update(
        {
            "ra": form.ra.data
        },
        {
            "$set": {
                "name": form.name.data.upper(),
                "age": form.age.data,
            },
            "$addToSet": {"courses": {
                "campus": form.campus.data.upper(),
                "county": form.county.data,
                "course": form.course.data.upper(),
                "modality": form.modality.data.upper(),
                "level": form.level.data.upper(),
                "start_date": form.start_date.data,
            }},
        },
        upsert=True,
        return_document=ReturnDocument.AFTER
    )

    if query:
        # Armazenando dados atualizados no cache
        cache.set("student_get" + str(form.ra.data), query)

        return True

    return False


def student_delete(form: Form) -> dumps:
    """
    Serializer que deleta cursos de estudantes e estudantes sem cursos
    :return: json
    """
    collection_students = mongo.db.students

    query = collection_students.find_one_and_update(
        {
            "ra": form.ra.data,
            "courses.campus": form.campus.data.upper(),
        },
        {
            "$pull": {
                "courses": {
                    "campus": form.campus.data.upper(),
                }
            }
        },
        return_document=ReturnDocument.AFTER
    )

    if query is not None:
        collection_students.delete_one(
            {
                "_id": query["_id"],
                "courses": {"$size": 0},
            }
        )

        return True

    return False


def modality_get(modality: str, date_start: datetime, date_end: datetime) -> dumps:
    """
    Serializer que busca itens com modalidade em período
    :param modality: modalidade desejada
    :param date_start: data inicial
    :param date_end: data final
    :return: json
    """
    collection_students = mongo.db.students

    query = collection_students.aggregate([
        {"$project": {"_id": 0}},
        {"$unwind": "$courses"},
        {
            "$match":
                {
                    "courses.modality": modality,
                    "courses.start_date": {
                        "$gte": date_start,
                        "$lte": date_end,
                    }
                }
        },
        {"$sort": {"courses.start_date": -1}},
    ])

    return dumps(query)


def campus_courses_get(campus: str) -> dumps:
    """
    Serializer que busca por cursos de um campus
    :param campus: campus desejado
    :return: json
    """
    collection_students = mongo.db.students

    query = collection_students.aggregate([
        {"$project": {"_id": 0, "courses": 1}},
        {"$unwind": "$courses"},
        {"$match": {"courses.campus": campus.upper()}},
        {"$group": {
            "_id": "$courses.campus",
            "courses": {"$addToSet": "$courses.course"}
        }},
        {"$unwind": "$courses"},
        {"$sort": {"courses": 1}},

    ])

    return dumps(query)


def campus_students_get(campus: str, date_start: datetime, date_end: datetime) -> dumps:
    """
    Serializer que busca pela quantidade de estudentes de um campus num período
    :param campus: campus desejado
    :param date_start: data inicial
    :param date_end: date final
    :return: json
    """
    collection_students = mongo.db.students

    query = collection_students.aggregate([
        {"$project": {"_id": 0}},
        {
            "$match":
                {
                    "courses.campus": campus.upper(),
                    "courses.start_date": {
                        "$gte": date_start,
                        "$lte": date_end,
                    }
                }
        },
        {"$group": {"_id": campus.upper(), "count": {"$sum": 1}}},
    ])

    return dumps(query)
