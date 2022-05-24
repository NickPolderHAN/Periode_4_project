from flask import Flask, render_template, request
from Python.sorteerknoppen import sorteerknoppen

app = Flask(__name__, template_folder='../templates', static_folder='../static')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/graphs", methods=["POST", "GET"])
def graphs():
    return render_template('graphs.html')


@app.route("/infopagina", methods=["POST", "GET"])
def learn_more():
    return render_template('learnmore.html')


@app.route("/database_inladen", methods=["POST", "GET"])
def table():
    return render_template('table.html')


@app.route("/table", methods=["POST", "GET"])
def filter_resultaten():
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
