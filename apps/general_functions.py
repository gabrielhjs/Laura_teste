"""
Módulo que contém funções que retornam dados largamente repetidos no projeto
"""

from flask import json


def mimetype() -> str:
    """
    Retorna o formato dos dados que são encaminhados para o cliente na resposta http
    :return: formato dos dados
    """
    return "application/json"


def wrong_date_format_message():
    """
    Retorna o json da mensagem de erro para quando o usuário insere um parâmetro de data num formato incorreto
    :return: mensagem no formato json
    """
    return json.dumps({"message": "Wrong dates format. Correct format is aaaa-mm-dd!", "status": "error"})


def success_message():
    """
    Retorna o json da mensagem de sucesso para quando o usuário faz alguma alteração nos dados do banco
    :return: mensagem no formato json
    """
    return json.dumps({"message": "Operation performed successfully", "status": "success"})


def data_not_found_message():
    """
    Retorna o json da mensagem de erro para quando o sistema não encontrou os dados especificados no banco
    :return: mensagem no formato json
    """
    return json.dumps({"message": "Data not found", "status": "error"})
