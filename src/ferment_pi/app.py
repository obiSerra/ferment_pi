from database import get_last_temperature

import subprocess

from flask import Flask

app = Flask(__name__)


# set_scheduler(func=run, seconds=10)
# subprocess.Popen(["python3","-r","some.file"])


@app.route('/')
def hello():
    temperature = get_last_temperature()
    return {'temperature': temperature}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
