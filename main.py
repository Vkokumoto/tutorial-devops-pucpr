"""
Aplicação FastAPI para demonstração de Continuous Integration com GitHub Actions.
"""

import random
from fastapi import FastAPI

app = FastAPI()


# http://127.0.0.1:8000/helloworld
@app.get("/helloworld")
async def root():
    '''Endpoint que retorna a mensagem 'Hello World'.'''
    return {"message": "Hello World"}


# http://127.0.0.1:8000/funcaoteste
@app.get("/funcaoteste")
async def funcaoteste():
    '''Endpoint de teste que retorna um número aleatório e um valor booleano.'''
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}
