from FlaskBlueprintTemplateApp import create_app
from flask_cors import CORS

app = create_app()

CORS(
    app,
    resources = {
        r"/*" : {"origins": "*"}
    }
)

import sqlite3
from flask import g

if __name__ == '__main__':
    app.run(debug=False)
