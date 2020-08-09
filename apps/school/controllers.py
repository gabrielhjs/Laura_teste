"""
Módulo que contém os controllers do aplicativo school. Responsável por receber os parâmetros de rota, executar os
serializers e retorna uma resposta http para o cliente
"""

from flask import Response, Blueprint, request, json
from datetime import datetime

from ..general_functions import mimetype, wrong_date_format_message, success_message, data_not_found_message

from . import serializers
from .forms import FormUserCreate, FormUserDelete


# Criando variável de rotas
school_routes = Blueprint("school", __name__, url_prefix="/api/school")


@school_routes.route("/student/<int:ra>/", methods=("GET",))
def student_get(ra: int) -> Response:
    """
    Controller de acesso as informações e cadastro de alunos nos cursos
    """
    response = serializers.student_get(ra)

    return Response(response, status=200, mimetype=mimetype())


@school_routes.route("/student/new/", methods=("POST",))
def student_post() -> Response:
    """
    Controller de cadastro e atualização de alunos
    """
    form = FormUserCreate(request.form)

    if form.validate():
        status = serializers.student_post(form)

        if status:
            return Response(success_message(), status=202, mimetype=mimetype())

        return Response(data_not_found_message(), status=202, mimetype=mimetype())

    response = []

    for field, messages in form.errors.items():
        for message in messages:
            response.append(
                {"field": field, "error": message}
            )

    response = json.dumps(response)

    return Response(response, status=422, mimetype=mimetype())


@school_routes.route("/student/delete/", methods=("POST",))
def student_delete() -> Response:
    """
    Controller de cadastro e atualização de alunos
    """
    form = FormUserDelete(request.form)

    if form.validate():
        status = serializers.student_delete(form)

        if status:
            return Response(success_message(), status=202, mimetype=mimetype())

        return Response(data_not_found_message(), status=202, mimetype=mimetype())

    response = []

    for field, messages in form.errors.items():
        for message in messages:
            response.append(
                {"field": field, "error": message}
            )

    response = json.dumps(response)

    return Response(response, status=422, mimetype=mimetype())


@school_routes.route("/modality/<modality>/<date_start>/<date_end>/", methods=("GET",))
def modality_get(modality: str, date_start: str, date_end: str) -> Response:
    """
    Controller de acesso as informações de uma modalidade num determinado período
    """
    try:
        date_start = datetime.strptime(date_start, "%Y-%m-%d")
        date_end = datetime.strptime(date_end, "%Y-%m-%d")

    except ValueError:
        response = wrong_date_format_message()

        return Response(response, status=422, mimetype=mimetype())

    else:
        response = serializers.modality_get(modality, date_start, date_end)

        return Response(response, status=200, mimetype="application/json")


@school_routes.route("/campus/<campus>/", methods=("GET",))
def campus_courses_get(campus: str) -> Response:
    """
    Controller de acesso as informações dos cursos de cada campus
    """
    response = serializers.campus_courses_get(campus)

    return Response(response, status=200, mimetype=mimetype())


@school_routes.route("/campus/students/<campus>/<date_start>/<date_end>/", methods=("GET",))
def campus_students_get(campus: str, date_start: str, date_end: str) -> Response:
    """
    Controller de acesso as informações da quantidade de alunos de cada campus
    """
    try:
        date_start = datetime.strptime(date_start, "%Y-%m-%d")
        date_end = datetime.strptime(date_end, "%Y-%m-%d")

    except ValueError:
        response = wrong_date_format_message()

        return Response(response, status=422, mimetype=mimetype())

    else:
        response = serializers.campus_students_get(campus, date_start, date_end)

        return Response(response, status=200, mimetype=mimetype())
