from fastapi import FastAPI
from pydantic import BaseModel

#para rodar o servidor, execute o seguinte comando no terminal: python -m uvicorn main:app --reload

app = FastAPI()

tarefas = []
proximo_id = 1


class TarefaNova(BaseModel):
    titulo: str


@app.get("/")
def raiz():
    return {"mensagem": "Olá! A API do Gerenciador de Tarefas está funcionando."}


@app.post("/tarefas", status_code=201)
def criar_tarefa(dados: TarefaNova):
    global proximo_id
    tarefa = {"id": proximo_id, "titulo": dados.titulo, "concluida": False}
    tarefas.append(tarefa)
    proximo_id += 1
    return tarefa


@app.get("/tarefas")
def listar_tarefas():
    return tarefas