import mysql.connector

class sorteerknoppen:
    def get_data(self, e_value_min, e_value_max, percent_identity_min,
                 percent_identity_max, organism, protein):
        """

        :param e_value_min: String -> contains a minimum e-value
        :param e_value_max: String -> contains a maximum e-value
        :param percent_identity_min: String -> contains a minimum
                                               identity percentage
        :param percent_identity_max: String -> contains a maximum
                                               identity percentage
        :param organism:
        :param protein:
        :return:
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

        if e_value_min != '' and e_value_max != '':
            if percent_identity_min != '' and percent_identity_max != '':
                if organism != '':
                    sql = f"select * from hits where e_value > {e_value_min} "\
                          f"and e_value < {e_value_max} and " \
                          f"identitypercentage > {percent_identity_min} and " \
                          f"identitypercentage < {percent_identity_max} and " \
                          f"organisme like '%{organism}%'"
                    mycursor.execute(sql)
                elif protein != '':
                    sql = f"select * from hits where e_value > {e_value_min} "\
                          f"and e_value < {e_value_max} and " \
                          f"identitypercentage > {percent_identity_min} and " \
                          f"identitypercentage < {percent_identity_max} and " \
                          f"eiwit like '%{protein}%'"
                    mycursor.execute(sql)
                elif organism and protein != '':
                    sql = f"select * from hits where e_value > {e_value_min} "\
                          f"and e_value < {e_value_max} and " \
                          f"identitypercentage > {percent_identity_min} and " \
                          f"identitypercentage < {percent_identity_max} and " \
                          f"organisme like '%{organism}%' and eiwit like " \
                          f"'%{protein}%'"
                    mycursor.execute(sql)
                else:
                    sql = f"select * from hits where e_value > {e_value_min} "\
                          f"and e_value < {e_value_max} and " \
                          f"identitypercentage > {percent_identity_min} and " \
                          f"identitypercentage < {percent_identity_max}"
                    mycursor.execute(sql)
            elif organism != '':
                if protein != '':
                    sql = f"select * from hits where e_value > {e_value_min} "\
                          f"and e_value < {e_value_max} and organisme like " \
                          f"'%{organism}%' and eiwit like '%{protein}%'"
                    mycursor.execute(sql)
                else:
                    sql = f"select * from hits where e_value > {e_value_min} "\
                          f"and e_value < {e_value_max} and organisme like " \
                          f"'%{organism}%'"
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
                          f"{percent_identity_max} and organisme like " \
                          f"'%{organism}%' and eiwit like '%{protein}%'"
                    mycursor.execute(sql)
                else:
                    sql = f"select * from hits where identitypercentage >" \
                          f"{percent_identity_min} and identitypercentage <" \
                          f"{percent_identity_max} and organisme like " \
                          f"'%{organism}%'"
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
                sql = f"select * from hits where organisme like " \
                      f"'%{organism}%' and eiwit like '%{protein}%'"
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
