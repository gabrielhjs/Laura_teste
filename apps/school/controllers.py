"""
Módulo que contém os controllers do aplicativo school
"""

from flask import json, Response
from flask.views import MethodView


class User(MethodView):
    """
    Controller de acesso as informações e cadastro de alunos nos cursos
    """

    def get(self, ra: int) -> Response:
        """
        Função de busca por aluno
        :param ra: ra do aluno desejado
        :return: json com os dados do aluno
        """

        response = json.dumps({"message": "dados de um aluno", "ra": ra})

        return Response(response, status=200, mimetype="application/json")

    def post(self, request) -> Response:
        pass
