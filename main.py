from fastapi import FastAPI

app = FastAPI(title="AutoClip Backend")

@app.get("/")
def home():
    return {"message": "AutoClip Backend Online"}

@app.get("/health")
def health():
    return {"status": "ok"}

