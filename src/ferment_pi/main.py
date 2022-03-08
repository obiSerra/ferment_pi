from os import path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from ferment_pi.database import get_last_temperature, save_temperature

app = FastAPI()
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FRONTEND_PATH = path.join(path.dirname(__file__),
                          "./frontend_build")


@app.get('/api/temperature')
def last_temperature() -> dict:
    """
    Return the last measured temperature from the database

        Returns:
                dict: { 'data': <dict> }
    """
    temperature = get_last_temperature()
    return {'data': temperature}


@app.get('/api/save')
def save_temperature_api() -> dict:
    temperature = save_temperature('10', '99')
    return temperature


# Static files
app.mount("/", StaticFiles(directory=FRONTEND_PATH, html=True))
