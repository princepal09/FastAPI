from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Patient Managment System Api"}


@app.get("/about")
def about():
    return {"message": "A Fully Functional API To manage your patient records"}
