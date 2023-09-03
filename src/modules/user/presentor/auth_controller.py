from src.main import app


@app.post("/user/login")
def login():
    try:
        return {"message": "Hello"}
    except IndexError:
        print("hello")


@app.delete("/user/logout")
def logout():
    try:
        return {"message": "Hello"}

    except IndexError:
        print("Hello")
