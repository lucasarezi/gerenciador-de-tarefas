from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
    return {"Mensagem": "O FastAPI está funcionando!"}