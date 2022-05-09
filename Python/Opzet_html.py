from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def hoofdpagina():
    return


@app.route("/resultaten", methods=["POST", "GET"])
def resultaten():
    return


@app.route("/blast_pagina", methods=["POST", "GET"])
def blast_pagina():
    return


@app.route("/database_inladen", methods=["POST", "GET"])
def database_inladen():
    return


if __name__ == '__main__':
    app.run()
