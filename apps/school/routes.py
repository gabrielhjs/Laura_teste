"""
Módulo de rotas do aplicativo school
"""

from flask import Blueprint

from .controllers import User


# Criando variável de rotas
school_routes = Blueprint("school", __name__)

# Inserindo as rotas do aplicativo
school_routes.add_url_rule("/<int:ra>", "index", User.as_view())
