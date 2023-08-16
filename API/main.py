from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return "Nguyen Tuan Anh dep trai"