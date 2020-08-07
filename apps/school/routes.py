"""
Módulo de rotas do aplicativo school
"""

from flask import Blueprint

from .controllers import User, Modality


# Criando variável de rotas
school_routes = Blueprint("school", __name__)

# Inserindo as rotas do aplicativo
school_routes.add_url_rule("/", "index", User.as_view("index"))
school_routes.add_url_rule(
    "/modality",
    "modality",
    Modality.as_view("modality")
)
