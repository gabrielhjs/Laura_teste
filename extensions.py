"""
Módulo de extensões do aplicativo
"""
from flask_pymongo import PyMongo
from flask_caching import Cache

# Criando variável de conexão com o banco de dados MongoDB
mongo = PyMongo()


# Criando cache menager
cache = Cache()
