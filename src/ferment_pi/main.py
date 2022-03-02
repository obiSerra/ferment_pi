from os import path
from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from ferment_pi.database import get_last_temperature

app = FastAPI()

FRONTEND_PATH = path.join(path.dirname(__file__),
                          "./frontend_build")


@app.get('/api/temperature')
def last_temperature():
    temperature = get_last_temperature()
    return {'temperature': temperature}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


app.mount("/", StaticFiles(directory=FRONTEND_PATH, html=True))
