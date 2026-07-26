from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI(title="AutoClip Backend")


@app.get("/")
def home():
    return {"message": "AutoClip Backend Online"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/process")
def process():
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={
            "status": "accepted",
            "message": "Processamento iniciado com sucesso."
        },
    )
