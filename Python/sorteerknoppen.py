import mysql.connector


class SorteerKnoppen:
    def __init__(self):
        self.__result = ''

    def load_page(self):
        # makes a connection to the database.
        mydb = mysql.connector.connect(
            host="145.74.104.145",
            user="pwtit",
            password="pwd123",
            database="pwtit",
            auth_plugin='mysql_native_password'
        )
        mycursor = mydb.cursor()

        sql = f"select * from hits"
        mycursor.execute(sql)
        self.__result = mycursor.fetchall()
        return self.__result


    def get_data(self, e_value_min, e_value_max, percent_identity_min,
                 percent_identity_max, organism, protein):
        """ Checks all parameters to execute specific queries and
        returns a list containing data from the database.

        :param e_value_min: String -> contains a minimum e-value
        :param e_value_max: String -> contains a maximum e-value
        :param percent_identity_min: String -> contains a minimum
                                               identity percentage
        :param percent_identity_max: String -> contains a maximum
                                               identity percentage
        :param organism: String -> contains a organism
        :param protein: String -> contains a protein
        :return: result -> List -> contains the data
        """
        # makes a connection to the database.
        mydb = mysql.connector.connect(
            host="145.74.104.145",
            user="pwtit",
            password="pwd123",
            database="pwtit",
            auth_plugin='mysql_native_password'
        )
        mycursor = mydb.cursor()

        # checks all parameters and executes specific queries.
        try:
            if e_value_min != '' and e_value_max != '':
                if percent_identity_min != '' and percent_identity_max != '':
                    if organism != '':
                        sql = f"select * from hits where e_value >= " \
                              f"{e_value_min} and e_value <= {e_value_max} " \
                              f"and identitypercentage >= " \
                              f"{percent_identity_min} and " \
                              f"identitypercentage <= {percent_identity_max} "\
                              f"and organisme like '%{organism}%'"
                        mycursor.execute(sql)
                    elif protein != '':
                        sql = f"select * from hits where e_value >= " \
                              f"{e_value_min} and e_value <= {e_value_max} " \
                              f"and identitypercentage >= " \
                              f"{percent_identity_min} and " \
                              f"identitypercentage <= {percent_identity_max} "\
                              f"and eiwit like '%{protein}%'"
                        mycursor.execute(sql)
                    elif organism and protein != '':
                        sql = f"select * from hits where e_value >= " \
                              f"{e_value_min} and e_value <= {e_value_max} " \
                              f"and identitypercentage >= " \
                              f"{percent_identity_min} and " \
                              f"identitypercentage <= {percent_identity_max} "\
                              f"and organisme like '%{organism}%' and eiwit " \
                              f"like '%{protein}%'"
                        mycursor.execute(sql)
                    else:
                        sql = f"select * from hits where e_value >= " \
                              f"{e_value_min} and e_value <= {e_value_max} " \
                              f"and identitypercentage >= " \
                              f"{percent_identity_min} and " \
                              f"identitypercentage <= {percent_identity_max}"
                        mycursor.execute(sql)
                elif organism != '':
                    if protein != '':
                        sql = f"select * from hits where e_value >= " \
                              f"{e_value_min} and e_value <= {e_value_max} " \
                              f"and organisme like '%{organism}%' and eiwit " \
                              f"like '%{protein}%'"
                        mycursor.execute(sql)
                    else:
                        sql = f"select * from hits where e_value >= " \
                              f"{e_value_min} and e_value <= {e_value_max} " \
                              f"and organisme like '%{organism}%'"
                        mycursor.execute(sql)
                elif protein != '':
                    sql = f"select * from hits where e_value >= " \
                          f"{e_value_min} and e_value <= {e_value_max} and " \
                          f"eiwit like '%{protein}%'"
                    mycursor.execute(sql)
                else:
                    sql = f"select * from hits where e_value >= " \
                          f"{e_value_min} and e_value <= {e_value_max}"
                    mycursor.execute(sql)
            elif percent_identity_min != '' and percent_identity_max != '':
                if organism != '':
                    if protein != '':
                        sql = f"select * from hits where " \
                              f"identitypercentage >= {percent_identity_min} "\
                              f"and identitypercentage <= " \
                              f"{percent_identity_max} and organisme like " \
                              f"'%{organism}%' and eiwit like '%{protein}%'"
                        mycursor.execute(sql)
                    else:
                        sql = f"select * from hits where identitypercentage " \
                              f">= {percent_identity_min} and " \
                              f"identitypercentage <= {percent_identity_max} "\
                              f"and organisme like '%{organism}%'"
                        mycursor.execute(sql)
                elif protein != '':
                    sql = f"select * from hits where identitypercentage >=" \
                          f"{percent_identity_min} and identitypercentage <=" \
                          f"{percent_identity_max} and eiwit like " \
                          f"'%{protein}%'"
                    mycursor.execute(sql)
                else:
                    sql = f"select * from hits where identitypercentage >=" \
                          f"{percent_identity_min} and identitypercentage <=" \
                          f"{percent_identity_max}"
                    mycursor.execute(sql)
            elif organism != '':
                if protein != '':
                    sql = f"select * from hits where organisme like " \
                          f"'%{organism}%' and eiwit like '%{protein}%'"
                    mycursor.execute(sql)
                else:
                    sql = f"select * from hits where organisme like " \
                          f"'%{organism}%'"
                    mycursor.execute(sql)
            elif protein != '':
                sql = f"select * from hits where eiwit like '%{protein}%'"
                mycursor.execute(sql)
            else:
                sql = f"select * from hits"
                mycursor.execute(sql)

            # fetches all results from the queries.
            self.__result = mycursor.fetchall()
            return self.__result

        except:
            return self.__result
