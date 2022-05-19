import mysql.connector
from flask import Flask, request, render_template


def get_data(e_value_min, e_value_max, percent_identity_min, percent_identity_max, organism, protein):
    mydb = mysql.connector.connect(
        host="145.74.104.145",
        user="pwtit",
        password="pwd123",
        database="pwtit"
    )
    mycursor = mydb.cursor()

    e_value_min = str(request.form.get("e_value_min").strip().replace('\n', ''))
    e_value_max = str(request.form.get("e_value_max").strip().replace('\n', ''))
    percent_identity_min = str(request.form.get("percent_identity_min").strip().replace('\n', ''))
    percent_identity_max = str(request.form.get("percent_identity_max").strip().replace('\n', ''))
    organism = str(request.form.get("organism").strip().replace('\n', ''))
    protein = str(request.form.get("protein").strip().replace('\n', ''))

    if e_value_min != '' and e_value_max != '':
        if percent_identity_min != '' and percent_identity_max != '':
            if organism != '':
                sql = f"select * from hits where e_value > {e_value_min} and " \
                      f"e_value < {e_value_max} and identitypercentage > " \
                      f"{percent_identity_min} and identitypercentage < " \
                      f"{percent_identity_max} and organisme like '%{organism}%'"
                mycursor.execute(sql)
            elif protein != '':
                sql = f"select * from hits where e_value > {e_value_min} and" \
                      f"e_value < {e_value_max} and identitypercentage >" \
                      f"{percent_identity_min} and identitypercentage <" \
                      f"{percent_identity_max} and eiwit like '%{protein}%'"
                mycursor.execute(sql)
            elif organism and protein != '':
                sql = f"select * from hits where e_value > {e_value_min} and" \
                      f"e_value < {e_value_max} and identitypercentage >" \
                      f"{percent_identity_min} and identitypercentage <" \
                      f"{percent_identity_max} and organisme like '%{organism}%'" \
                      f"and eiwit like '%{protein}%"
                mycursor.execute(sql)
            else:
                sql = f"select * from hits where e_value > {e_value_min} and" \
                      f"e_value < {e_value_max} and identitypercentage >" \
                      f"{percent_identity_min} and identitypercentage <" \
                      f"{percent_identity_max}"
                mycursor.execute(sql)
        elif organism != '':
            if protein != '':
                sql = f"select * from hits where e_value > {e_value_min} and" \
                      f"e_value < {e_value_max} and organisme like '%{organism}%'" \
                      f"and eiwit like '%{protein}%'"
                mycursor.execute(sql)
            else:
                sql = f"select * from hits where e_value > {e_value_min} and" \
                      f"e_value < {e_value_max} and organisme like '%{organism}%'"
                mycursor.execute(sql)
        elif protein != '':
            sql = f"select * from hits where e_value > {e_value_min} and" \
                  f"e_value < {e_value_max} and eiwit like '%{protein}%'"
            mycursor.execute(sql)
        else:
            sql = f"select * from hits where e_value > {e_value_min} and" \
                  f"e_value < {e_value_max}"
            mycursor.execute(sql)
    elif percent_identity_min != '' and percent_identity_max != '':
        if organism != '':
            if protein != '':
                sql = f"select * from hits where identitypercentage > " \
                      f"{percent_identity_min} and identitypercentage <" \
                      f"{percent_identity_max} and organisme like '%{organism}%'" \
                      f"and eiwit like '%{protein}%'"
                mycursor.execute(sql)
            else:
                sql = f"select * from hits where identitypercentage >" \
                      f"{percent_identity_min} and identitypercentage <" \
                      f"{percent_identity_max} and organisme like '%{organism}%'"
                mycursor.execute(sql)
        elif protein != '':
            sql = f"select * from hits where identitypercentage >" \
                  f"{percent_identity_min} and identitypercentage <" \
                  f"{percent_identity_max} and eiwit like '%{protein}%'"
            mycursor.execute(sql)
        else:
            sql = f"select * from hits where identitypercentage >" \
                  f"{percent_identity_min} and identitypercentage <" \
                  f"{percent_identity_max}"
            mycursor.execute(sql)
    elif organism != '':
        if protein != '':
            sql = f"select * from hits where organisme like '%{organism}%'" \
                  f"and eiwit like '%{protein}%'"
            mycursor.execute(sql)
        else:
            sql = f"select * from hits where organisme like '%{organism}%'"
            mycursor.execute(sql)
    elif protein != '':
        sql = f"select * from hits where eiwit like '%{protein}%'"
        mycursor.execute(sql)
    else:
        sql = f"select * from hits"
        mycursor.execute(sql)

    result = mycursor.fetchall()
    return result
