"""Flask App Project."""
import threading
import time

from flask import Flask, jsonify

import sqllite

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    json_data = {'Hello': 'World!'}
    return jsonify(json_data)

print('pproc-start')
sqllite.proc_start()
if __name__ == '__main__':



    app.run()
