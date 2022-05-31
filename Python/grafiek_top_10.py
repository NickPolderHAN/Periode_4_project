import mysql.connector as mq


class TopTen:
    def __init__(self):
        self.__protein = []
        self.__protein_amount = []
        self.__organism = []
        self.__organism_amount = []

    def data_top_ten_proteins(self):
        """
        Haalt de top 10 proteins met de bijbehorende
        frequenties uit de database en returned deze
        in twee lists.

        :param self.__protein -> List -> De top 10 eiwitten
                                        uit de database.

        :param self.__protein_amount -> List -> Het aantal
                                        van de top 10 eiwitten
                                        uit de database.

        :return self.__protein, self.__protein_amount
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
                    self.__protein.append(result)

                elif counter == 1:
                    self.__protein_amount.append(result)

        return self.__protein, self.__protein_amount

    def data_top_ten_organisms(self):
        """
        Haalt de top 10 organismen met de bijbehorende
        frequenties uit de database en returned deze in twee lists.

        :param self.__organism -> list -> De top 10 organismen
                                            uit de database.

        :param self.__organism_amount -> list -> Het aantal van de
                                                top 10 organismen
                                                uit de database.

        :return return self.__organism, self.__organism_amount
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
                    self.__organism.append(result)
                elif counter == 1:
                    self.__organism_amount.append(result)

        return self.__organism, self.__organism_amount
