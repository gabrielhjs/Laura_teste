"""
Módulo que contém os controllers do aplicativo school
"""

from flask import json, Response, jsonify, request
from flask.views import MethodView
from bson.json_util import dumps
from datetime import datetime

from extensions import mongo


class User(MethodView):
    """
    Controller de acesso as informações e cadastro de alunos nos cursos
    """

    def get(self) -> Response:
        """
        Função de busca por aluno
        """

        response = json.dumps({"message": "dados de um aluno"})

        return Response(response, status=200, mimetype="application/json")

    def post(self) -> Response:
        pass


class Modality(MethodView):
    """
    Controller de acesso as informações de modalidades
    """

    def get(self) -> Response:
        """
        Função de busca por modalidade com filtros de data
        """

        students = mongo.db.students

        modality = request.args.get("modality")
        date_start = request.args.get("date_start")
        date_end = request.args.get("date_end")

        query = students.aggregate([
            {"$project": {"_id": 0}},
            {
                "$match":
                    {
                        "courses.modality": {"$regex": ".*" + modality + ".*"},
                        "courses.start_date": {
                            "$gte": datetime.strptime(date_start, "%Y-%m-%d"),
                            "$lte": datetime.strptime(date_end, "%Y-%m-%d"),
                        }
                    }
            },
            {"$sort": {"courses.start_date": -1}},
        ])

        response = dumps(query)

        return Response(response, status=200, mimetype="application/json")

    def post(self) -> Response:
        pass
