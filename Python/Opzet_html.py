from flask import Flask, render_template, request
from Python.sorteerknoppen import sorteerknoppen

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

@app.route("/table", methods=["POST", "GET"])
def table():
    sk = sorteerknoppen()
    if request.method == "POST":
        e_value_min = str(request.form.get("e_value_min").strip().replace('\n', ''))
        e_value_max = str(request.form.get("e_value_max").strip().replace('\n', ''))
        percent_identity_min = str(request.form.get("percent_identity_min").strip().replace('\n', ''))
        percent_identity_max = str(request.form.get("percent_identity_max").strip().replace('\n', ''))
        organism = str(request.form.get("organism").strip().replace('\n', ''))
        protein = str(request.form.get("protein").strip().replace('\n', ''))
        result = sk.get_data(e_value_min, e_value_max, percent_identity_min,
                             percent_identity_max, organism, protein)
    return render_template("table.html", data=result)


if __name__ == '__main__':
    app.run()
