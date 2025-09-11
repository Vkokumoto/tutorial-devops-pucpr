"""
Aplicação FastAPI para demonstração de Continuous Integration com GitHub Actions.
"""

import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool


# http://127.0.0.1:8000/helloworld
@app.get("/helloworld")
async def root():
    '''Endpoint que retorna a mensagem 'Hello World'.'''
    return {"message": "Hello World"}


# http://127.0.0.1:8000/funcaoteste
@app.get("/funcaoteste")
async def funcaoteste():
    '''Endpoint de teste que retorna um número aleatório e um valor booleano.'''
    return {"teste": True, "num_aleatorio": random.randint(0, 55000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    '''Endpoint de teste que retorna um estudante.'''
    return estudante

@app.put("estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    '''Endpoint de teste que atualiza um estudante.'''
    return id_estudante > 0

@app.delete("estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    '''Endpoint de teste que deleta um estudante.'''
    return id_estudante > 0
