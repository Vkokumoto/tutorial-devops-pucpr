"""Módulo principal da aplicação FastAPI."""
import random

from fastapi import FastAPI

app = FastAPI()


# http://127.0.0.1:8000/helloworld
@app.get("/helloworld")
async def root():
    """Executa a lógica X."""
    return {"message": "Hello World"}


# http://127.0.0.1:8000/funcaoteste
@app.get("/funcaoteste")
async def funcaoteste():
    """Executa a lógica X."""
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}
