"""
Módulo de rotas do aplicativo school
"""

from flask import Blueprint

from . import controllers


# Criando variável de rotas
school_routes = Blueprint("school", __name__)

# Inserindo as rotas do aplicativo
school_routes.add_url_rule("/student/<int:ra>", "student", controllers.Student.as_view("student"))

school_routes.add_url_rule(
    "/modality/<modality>/<date_start>/<date_end>/",
    "modality",
    controllers.Modality.as_view("modality")
)
school_routes.add_url_rule("/campus/<campus>/", "campus_courses", controllers.CampusCourses.as_view("campus_courses"))

school_routes.add_url_rule(
    "/campus/students/<campus>/<date_start>/<date_end>/",
    "campus_students",
    controllers.CampusStudents.as_view("campus_students")
)
