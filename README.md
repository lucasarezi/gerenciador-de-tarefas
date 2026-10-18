# Gerenciador de Tarefas

API REST para criar, listar e consultar tarefas por ID.
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

### Criar uma tarefa

Envie uma requisição `POST /tarefas` com um título entre 5 e 50 caracteres:

```json
{
  "titulo": "Organizar Casa"
}
```

A tarefa criada recebe um ID incremental e começa com `concluida: false`.

### Consultar uma tarefa pelo ID

Use o ID da tarefa no caminho da URL:

```text
GET /tarefas/1
```

Se o ID não existir, a API retorna o status `404 Not Found`.

## Status do projeto
- [x] Criar tarefa
- [x] Listar tarefas
- [x] Consultar tarefa por ID
- [ ] Atualizar tarefa
- [ ] Excluir tarefa
- [ ] Banco de dados (SQLite)
- [ ] Interface simples

## Próximos passos
Implementar as rotas de atualização e exclusão, adicionar persistência com SQLite e, depois, criar uma interface simples.
