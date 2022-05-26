import mysql.connector as mq


def data_top10_eiwitten():
    """Maakt connectie met de database en haalt de top 10 eiwitten uit de
      database. Deze resultaten voegt die toe aan een lijst.

    :return:
    eiwit -> lijst -> Staan alle eiwitten in van de sql statement
    aantal_eiwit -> lijst -> Staan alle aantallen in van de sql statement
    """
    db = mq.connect(host="145.74.104.145",
                    user="pwtit",
                    password="pwd123",
                    database="pwtit",
                    auth_plugin='mysql_native_password'
                    )
    dbcursor = db.cursor()
    #Haalt de top 10 eiwitten uit de database
    eiwitten = "Select eiwit, count(*) From hits Group by eiwit " \
               "Order by count(* ) desc limit 10"
    dbcursor.execute(eiwitten)
    eiwit_counter = dbcursor.fetchall()
    eiwit = []
    aantal_eiwit = []
    #Leest de resultaten door en voegt alles to aan de juiste lijsten
    for results in eiwit_counter:
        counter = 0
        for result in results:
            if counter == 0:
                counter += 1
                eiwit.append(result)
            elif counter == 1:
                aantal_eiwit.append(result)
    return eiwit, aantal_eiwit


def data_top10_organismen():
    """Maakt connectie met de database en haalt de top 10 organismen uit de
      database. Deze resultaten voegt die toe aan een lijst.

    :return:
    organisme -> lijst -> Staan alle organismen in van de sql statement
    aantal_organisme -> lijst -> Staan alle aantallen in van de sql statement
    """
    #Maakt connectie met de database
    db = mq.connect(host="145.74.104.145",
                    user="pwtit",
                    password="pwd123",
                    database="pwtit",
                    auth_plugin='mysql_native_password'
                    )
    dbcursor = db.cursor()
    #Haalt de top 10 organismen uit de database
    organismen = "Select organisme, count(*) From hits Group by organisme " \
                 "Order by count(*) desc limit 10"
    dbcursor.execute(organismen)
    organisme_counter = dbcursor.fetchall()
    organisme = []
    aantal_organsime = []
    #Leest de resultaten door en voegt alles to aan de juiste lijsten
    for results in organisme_counter:
        counter = 0
        for result in results:
            if counter == 0:
                counter += 1
                organisme.append(result)
            elif counter == 1:
                aantal_organsime.append(result)
    return organisme, aantal_organsime


def main():
    eiwit, aantal_eiwit = data_top10_eiwitten()
    organisme, aantal_organsime = data_top10_organismen()
    return eiwit, aantal_eiwit, organisme, aantal_organsime
