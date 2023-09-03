from src.main import app


@app.post("/")
def create_user():
    return {"message": "Hello, world!"}


@app.get("/")
def get_user():
    return {"message": "Hello, world!"}
