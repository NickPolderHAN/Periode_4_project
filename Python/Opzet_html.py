from flask import Flask, render_template, request
from Python.sorteerknoppen import SorteerKnoppen
from Python.grafiek_top_10 import top10

app = Flask(__name__, template_folder='../templates',
            static_folder='../static')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/graphs", methods=["POST", "GET"])
def graphs():
    grafiek = top10()
    eiwitten, aantal_eiwit = grafiek.data_top10_eiwitten()
    organismen, aantal_organisme = grafiek.data_top10_organismen()
    ei1, ei2, ei3, ei4, ei5, ei6, ei7, ei8, ei9, ei10, = eiwitten
    cei1, cei2, cei3, cei4, cei5, cei6, cei7, cei8, cei9, cei10 = aantal_eiwit
    org1, org2, org3, org4, org5, org6, org7, org8, org9, org10 = organismen
    corg1, corg2, corg3, corg4, corg5, corg6, corg7, corg8, corg9,\
        corg10 = aantal_organisme

    return render_template('graphs.html', ei1=ei1, ei2=ei2, ei3=ei3,
                           ei4=ei4, ei5=ei5, ei6=ei6, ei7=ei7, ei8=ei8,
                           ei9=ei9, ei10=ei10, org1=org1, org2=org2,
                           org3=org3, org4=org4, org5=org5, org6=org6,
                           org7=org7, org8=org8, org9=org9, org10=org10,
                           cei1=cei1, cei2=cei2, cei3=cei3, cei4=cei4,
                           cei5=cei5, cei6=cei6, cei7=cei7, cei8=cei8,
                           cei9=cei9, cei10=cei10, corg1=corg1,
                           corg2=corg2, corg3=corg3, corg4=corg4,
                           corg5=corg5, corg6=corg6, corg7=corg7,
                           corg8=corg8, corg9=corg9, corg10=corg10
                           )


@app.route("/infopagina", methods=["POST", "GET"])
def learn_more():
    return render_template('learnmore.html')


@app.route("/database_inladen", methods=["POST", "GET"])
def table():
    return render_template('table.html')


@app.route("/table", methods=["POST", "GET"])
def filter_resultaten():
    sk = SorteerKnoppen()

    if request.method == "POST":
        e_value_min = str(
            request.form.get("e_value_min").strip().replace('\n', ''))
        e_value_max = str(
            request.form.get("e_value_max").strip().replace('\n', ''))
        percent_identity_min = str(
            request.form.get("percent_identity_min").strip().replace('\n', ''))
        percent_identity_max = str(
            request.form.get("percent_identity_max").strip().replace('\n', ''))
        organism = str(request.form.get("organism").strip().replace('\n', ''))
        protein = str(request.form.get("protein").strip().replace('\n', ''))
        result = sk.get_data(e_value_min, e_value_max, percent_identity_min,
                             percent_identity_max, organism, protein)

    return render_template("table.html", data=result)


if __name__ == '__main__':
    app.run()
