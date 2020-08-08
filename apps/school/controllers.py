"""
Módulo que contém os controllers do aplicativo school
"""

from flask import Response
from flask.views import MethodView
from bson.json_util import dumps
from datetime import datetime

from extensions import mongo


class Student(MethodView):
    """
    Controller de acesso as informações e cadastro de alunos nos cursos
    """

    @staticmethod
    def get(ra) -> Response:
        """
        Função de busca por aluno
        """
        students = mongo.db.students

        query = students.find_one(
            {
                "ra": ra,
            }
        )

        response = dumps(query)

        return Response(response, status=200, mimetype="application/json")

    def post(self) -> Response:
        pass


class Modality(MethodView):
    """
    Controller de acesso as informações de modalidades
    """

    @staticmethod
    def get(modality, date_start, date_end) -> Response:
        """
        Função de busca por modalidade com filtros de data
        """

        try:
            date_start = datetime.strptime(date_start, "%Y-%m-%d")
            date_end = datetime.strptime(date_end, "%Y-%m-%d")

        except ValueError:
            response = dumps({"message": "Wrong dates format. Correct format is aaaa-mm-dd!", "error": 422})

            return Response(response, status=422, mimetype="application/json")

        else:
            students = mongo.db.students

            query = students.aggregate([
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

            response = dumps(query)

            return Response(response, status=200, mimetype="application/json")


class CampusCourses(MethodView):
    """
    Controller de acesso as informações dos cursos de cada campus
    """

    @staticmethod
    def get(campus) -> Response:
        """
        Função de busca por cursos de um determinado campus
        """

        students = mongo.db.students

        query = students.aggregate([
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

        response = dumps(query)

        return Response(response, status=200, mimetype="application/json")


class CampusStudents(MethodView):
    """
    Controller de acesso as informações da quantidade de alunos de cada campus
    """

    @staticmethod
    def get(campus, date_start, date_end) -> Response:
        """
        Função de busca pela quantidade de alunos de um determinado campus
        """

        try:
            date_start = datetime.strptime(date_start, "%Y-%m-%d")
            date_end = datetime.strptime(date_end, "%Y-%m-%d")

        except ValueError:
            response = dumps({"message": "Wrong dates format. Correct format is aaaa-mm-dd!", "error": 422})

            return Response(response, status=422, mimetype="application/json")

        else:
            students = mongo.db.students

            query = students.aggregate([
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

            response = dumps(query)

            return Response(response, status=200, mimetype="application/json")
