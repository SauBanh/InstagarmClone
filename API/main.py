from fastapi import FastAPI
from db import models
from db.database import engine

app = FastAPI()

@app.get('/')
def root():
    return "Nguyen Tuan Anh dep trai"

models.Base.metadata.create_all(engine)