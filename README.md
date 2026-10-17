# Gerenciador de Tarefas

API REST para criar, listar, consultar, atualizar e excluir tarefas.
Projeto de estudo em back-end com Python.

## Tecnologias
- Python 3.14
- FastAPI
- (SQLite, quando o banco for adicionado)

## Como rodar
1. Clone o repositório
2. Crie e ative o ambiente virtual
3. Instale as dependências: `pip install -r requirements.txt`
4. Inicie o servidor: `python -m uvicorn main:app --reload`
5. Abra `http://127.0.0.1:8000/docs` para testar as rotas

## Rotas
| Método | Rota | O que faz |
|---|---|---|
| GET | `/` | Verifica se a API está funcionando |
| POST | /tarefas | Cria uma tarefa |
| GET | /tarefas | Lista todas as tarefas |
| GET | /tarefas/{tarefa_id} | Consulta uma tarefa específica pelo ID |
| PATCH | /tarefas/{tarefa_id} | Atualiza o título de uma tarefa |
| DELETE | /tarefas/{tarefa_id} | Exclui uma tarefa |

### Criar uma tarefa

Envie uma requisição `POST /tarefas` com um título entre 5 e 50 caracteres:

```json
{
  "titulo": "Lavar a casa"
}
```

A tarefa criada recebe um ID incremental e começa com `concluida: false`.

### Consultar uma tarefa pelo ID

Use o ID da tarefa no caminho da URL:

```text
GET /tarefas/1
```

Se o ID não existir, a API retorna o status `404 Not Found`.

### Atualizar uma tarefa

Envie uma requisição `PATCH` usando o ID da tarefa e o novo título:

```text
PATCH /tarefas/1
```

```json
{
  "titulo": "Limpar a garagem"
}
```

O título deve ter entre 5 e 50 caracteres. Se o ID não existir, a API retorna o status `404 Not Found`.

### Excluir uma tarefa

Envie uma requisição `DELETE` usando o ID da tarefa:

```text
DELETE /tarefas/1
```

Se a tarefa for encontrada, a API retorna uma mensagem de sucesso. Se o ID não existir, retorna o status `404 Not Found`.

## Status do projeto
- [x] Criar tarefa
- [x] Listar tarefas
- [x] Consultar tarefa por ID
- [x] Atualizar tarefa
- [x] Excluir tarefa
- [ ] Banco de dados (SQLite)
- [ ] Interface simples

## Próximos passos
Adicionar persistência com SQLite e, depois, criar uma interface simples.
