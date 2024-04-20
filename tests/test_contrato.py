from datetime import datetime

import pytest
from pydantic import ValidationError

from src.contrato import Vendas


def test_vendas_com_dados_validos():
    dados_validos = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "valor": 100.50,
        "produto": "Produto X",
        "quantidade": 3,
        "categoria": "categoria1",
    }

    venda = Vendas(**dados_validos)

    assert venda.email == dados_validos["email"]
    assert venda.data == dados_validos["data"]
    assert venda.valor == dados_validos["valor"]
    assert venda.produto == dados_validos["produto"]
    assert venda.quantidade == dados_validos["quantidade"]
    assert venda.categoria == dados_validos["categoria"]


def test_vendas_com_dados_invalidos():
    dados_invalidos = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "valor": -100.50,
        "produto": "",
        "quantidade": -1,
        "categoria": "categoria3",
    }

    with pytest.raises(ValidationError):
        Vendas(**dados_invalidos)


def test_validacao_categoria():
    dados = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "valor": 100.50,
        "produto": "Produto Y",
        "quantidade": 1,
        "categoria": "categoria inexistente",
    }

    with pytest.raises(ValidationError):
        Vendas(**dados)
