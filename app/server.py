import os

from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from . import api

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{os.getenv("SQLITE_FILE", "")}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/graphql", methods=["GET"])
def playgroud():
    return (PLAYGROUND_HTML, 200)


@app.route("/graphql", methods=["POST"])
def do_graphql():
    data = request.get_json()

    success, result = graphql_sync(
        api.schema, data, context_value=request, debug=app.debug
    )

    return (jsonify(result), 200 if success else 400)


if __name__ == "__main__":
    app.run()

