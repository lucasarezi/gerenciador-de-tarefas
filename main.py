from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

#para rodar o servidor, execute o seguinte comando no terminal: python -m uvicorn main:app --reload

app = FastAPI()


@app.get("/")
def raiz():
    return {"mensagem": "Olá! A API do Gerenciador de Tarefas está funcionando."}