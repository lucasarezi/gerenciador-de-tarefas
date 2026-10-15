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
| POST | /tarefas | Cria uma tarefa |
| GET | /tarefas | Lista todas as tarefas |
| ... | ... | ... |

## Status do projeto
- [x] Criar tarefa
- [x] Listar tarefas
- [ ] Consultar tarefa por id
- [ ] Atualizar tarefa
- [ ] Excluir tarefa
- [ ] Banco de dados (SQLite)
- [ ] Interface simples

## Próximos passos
Estabilizar e testar todas as rotas da API e, depois, criar uma interface simples.
