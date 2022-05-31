import mysql.connector as mq


class top10():
    def __init__(self):
        self.__eiwit = []
        self.__aantal_eiwit = []
        self.__organisme = []
        self.__aantal_organisme = []

    def data_top10_eiwitten(self):
        """
        Haalt de top 10 eiwitten met het aantal daarvan uit de database
        en returnd twee lijsten met de data van de database.
        :return:
        eiwit -> list -> De top 10 eiwitten uit de database.
        aantal_eiwit -> list -> Het aantal van de top 10 eiwitten
                                uit de database.
        """
        # Maakt een connectie met de database.
        db = mq.connect(host="145.74.104.145",
                        user="pwtit",
                        password="pwd123",
                        database="pwtit",
                        auth_plugin='mysql_native_password'
                        )
        dbcursor = db.cursor()
        # Haalt de top 10 eiwitten uit de database
        eiwitten = "Select eiwit, count(*) From hits Group by eiwit " \
                   "Order by count(* ) desc limit 10"
        dbcursor.execute(eiwitten)
        eiwit_counter = dbcursor.fetchall()
        # Zet de resultaten in de goede lijsten
        for results in eiwit_counter:
            counter = 0
            for result in results:
                if counter == 0:
                    counter += 1
                    self.__eiwit.append(result)
                elif counter == 1:
                    self.__aantal_eiwit.append(result)
        return self.__eiwit, self.__aantal_eiwit

    def data_top10_organismen(self):
        """
        Haalt de top 10 organismen met het aantal daarvan uit de database
        en returnd twee lijsten met de data van de database.
        :return:
        organisme -> list -> De top 10 organismen uit de database.
        aantal_organsime -> list -> Het aantal van de top 10 organismen
                                uit de database.
        """
        # Maakt een connectie met de database.
        db = mq.connect(host="145.74.104.145",
                        user="pwtit",
                        password="pwd123",
                        database="pwtit",
                        auth_plugin='mysql_native_password'
                        )
        dbcursor = db.cursor()
        # Haalt de top 10 organisme uit de database
        organismen = "Select organisme, count(*) From hits Group by " \
                     "organisme Order by count(*) desc limit 10"
        dbcursor.execute(organismen)
        organisme_counter = dbcursor.fetchall()
        # Zet de resultaten in de goede lijsten
        for results in organisme_counter:
            counter = 0
            for result in results:
                if counter == 0:
                    counter += 1
                    self.__organisme.append(result)
                elif counter == 1:
                    self.__aantal_organisme.append(result)
        return self.__organisme, self.__aantal_organisme
