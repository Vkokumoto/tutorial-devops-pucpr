from unittest.mock import patch
import pytest

from src.main import (
    root, 
    funcaoteste, 
    create_estudante, 
    update_estudante, 
    delete_estudante, 
    Estudante)

"""Testes para a aplicação FastAPI do projeto."""

@pytest.mark.asyncio
async def test_root():
    """Teste do endpoint /helloworld."""
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_funcaoteste():
    """Teste do endpoint /funcaoteste."""
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}

@pytest.mark.asyncio
async def test_create_estudante():
    """Teste do endpoint /estudantes/cadastro."""
    estudante_teste = Estudante(name="Fulano", curso="ADS", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result

@pytest.mark.asyncio
async def test_update_estudante_negativo():
    """Teste do endpoint /estudantes/update."""
    result = await update_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_update_estudante_positivo():
    """Teste do endpoint /estudantes/update."""
    result = await update_estudante(10)
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    """Teste do endpoint /estudantes/delete."""
    result = await delete_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    """Teste do endpoint /estudantes/delete."""
    result = await delete_estudante(5)
    assert result
