import os

from flask import Flask, send_from_directory
from flask.helpers import safe_join

from database import get_last_temperature

app = Flask(__name__, static_url_path=None)


static = safe_join(
    os.path.dirname(__file__), 'frontend_build')

app.static_url_path = '/'
app.root_path = static

@app.route('/')
def home():
    print(static)
    return send_from_directory(static, 'index.html')


@app.route('/<path:path>')
def static_url(path):
    print("STATIC", path)
    if os.path.isdir(safe_join(static, path)):
        path = os.path.join(path, 'index.html')
    print("STATIC!!!!", path)
    return send_from_directory(static, path)


@app.route('/api/temperature')
def hello():
    temperature = get_last_temperature()
    return {'temperature': temperature}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
