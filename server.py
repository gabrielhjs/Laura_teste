"""
Arquivo de execução da aplicação
"""
from flask import Flask, json, Response

# Importando extensões da aplicação (banco de dados)
from extensions import mongo, cache

# Importando rotas dos aplicativos
from apps.school.controllers import school_routes


# Criando aplicação
app = Flask(__name__)
app.config.from_object("settings.Config")


# Iniciando conexão com o banco de dados
# Número máximo de itens: 10
# Defaul timeout: 500
mongo.init_app(app)
cache.init_app(app, config={"CACHE_TYPE": "simple", "CACHE_THRESHOLD": 10, "CACHE_DEFAULT_TIMEOUT": 500})


# Incluindo rotas de aplicativos
app.register_blueprint(school_routes)


# Criando rota de erro 404
@app.errorhandler(404)
def not_found(error) -> Response:
    response = json.dumps(
        {
            "error": error.name,
            "code": error.code,
            "description": error.description,
        }
    )
    return Response(response, status=404, mimetype="application/json")


# Código de execução da aplicação
if __name__ == "__main__":
    # Executando a aplicação
    app.run()
