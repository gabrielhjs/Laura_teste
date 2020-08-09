"""
Módulo de configurações do projeto
"""
import os
from dotenv import load_dotenv
from pathlib import Path


# Carregando variáveis de ambiente do arquivo env_file.env
env_path = Path('.') / 'env_file.env'
load_dotenv(dotenv_path=env_path)


class Config(object):
    """
    Classe de configuração da aplicação
    """

    # Configurando variável de conexão com o banco de dados
    MONGO_URI = str(os.getenv("SERVER_URI"))

    # Habilitando cache
    CACHE_TYPE = str(os.getenv("CACHE_TYPE"))  # O tipo "simple" está sendo usado apenas para demonstração
