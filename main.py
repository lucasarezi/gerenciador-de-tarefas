from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

#para rodar o servidor, execute o seguinte comando no terminal: python -m uvicorn main:app --reload

app = FastAPI()

tarefas = []
proximo_id = 1


class TarefaNova(BaseModel):
    titulo: str = Field(..., min_length=5, max_length=50)

#O Field() garante que o título da tarefa seja uma string com comprimento mínimo de 5 e máximo de 50 caracteres.

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


@app.get("/tarefas/{tarefa_id}")
def buscar_tarefas(tarefa_id: int):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.patch("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, dados: TarefaNova):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["titulo"] = dados.titulo
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")



@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefas.remove(tarefa)
            return {"mensagem": "Tarefa deletada com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")