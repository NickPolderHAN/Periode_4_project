import mysql.connector
import process_blast_results
import re
import Extract_excel_data
import time


class DatabaseInsert:
    def __init__(self):
        # gets the dictionary from the extract_excel_data script
        # containing the original sequences and assigns
        # it to a variable
        self.__excel_data_dict = Extract_excel_data.main()

        # contains all the individual hit data per blast.xml file.
        self.__hit_dict = {}

        # contains all the sequences with their id.
        self.__seq_dict = {}

        # used to check if a certain taxonomy is already present.
        self.__taxo_check = []

        # specifies the amount of files to be read (my_blast[num].xml)
        self.__file_amount = 98

        connect = mysql.connector.connect(host="145.74.104.145",
                                          user="pwtit",
                                          password="pwd123",
                                          database="pwtit")
        self.__cursor = connect.cursor()

        # calls the functions to get all the needed table data.
        print("Working.....")
        self.gather_sequences_from_dict()
        self.get_all_hits_taxonomy()
        self.insert_data_to_db()

        self.__cursor.close()

    # gets both the hits and taxonomy.
    def get_all_hits_taxonomy(self):
        """
        Calls the blast processor script to get all hit and taxonomy
        data from the .xml files, the amount of files has been
        specified in the init function.

        template: Blast [num]: [hit data per hit]

        return: added to the hit_dict as key: Blast [num].
        """
        file_counter = 0

        while file_counter < self.__file_amount:
            print(file_counter)
            time.sleep(1.0)
            file_counter += 1
            file_name = "my_blastx" + str(file_counter) + ".xml"
            key_name = "blast hits " + str(file_counter)

            # creates a BlastParser instance to gather hit data.
            bp = process_blast_results.BlastParser(file_name,
                                                   file_counter,
                                                   self.__seq_dict)

            hit_data = bp.get_all_attributes()
            self.__hit_dict[key_name] = hit_data
            self.insert_data_to_db()

        print("Finished getting all hit data from .xml files.")

    def gather_sequences_from_dict(self):
        """
        Stores all the original sequences to a dictionary and gives
        them an id (for example: id 1 and 2 are
        corresponding reads 1 and 2.)

        :return: seq_dict -> Dict -> Dictionary containing all the
                                    original sequences from the Excel
                                    data dictionary.

        """
        seq_dict = {}
        lijst_seq_per_rij = []
        counter = 0

        for value in self.__excel_data_dict.values():
            for item in value:
                if re.search('^[ATGC]+$', item):
                    lijst_seq_per_rij.append(item)

            counter += 1
            seq_dict[str(counter)] = lijst_seq_per_rij[0]
            seq_dict[str(counter + 100)] = lijst_seq_per_rij[1]
            lijst_seq_per_rij = []

        self.__seq_dict = seq_dict

    def insert_data_to_db(self):
        hit_query = "INSERT INTO hits values ("
        hit_string = ""

        taxo_query = "INSERT INTO taxonomy values ("
        taxo_string = ""

        seq_query = "INSERT INTO seq values ("
        seq_string = ""

        hit_list = ["score", "e_val", "idpercentage", "organism",
                    "eiwit", "accessie_code", "positives", "seq_id"]

        hit_counter = 1
        hd = self.__hit_dict
        for key in hd:
            for h_key in hd[key]:
                for i_key in hd[key][h_key]:
                    if i_key in hit_list:
                        if i_key != "seq_id":
                            string = str(hd[key][h_key][i_key])
                            string = string.replace("[", "")
                            string = string.replace("]", "")

                            if i_key == "accessie_code":
                                hit_string += "'"
                                string += "'"

                            hit_string += string
                            hit_string += ", "
                        else:
                            lineage = hd[key][h_key]["lineage"][0]
                            rank = hd[key][h_key]["rank"][0]
                            if lineage not in self.__taxo_check:
                                self.__taxo_check.append(lineage)
                                index = len(self.__taxo_check)

                                taxo_string += str(index) + ", "
                                taxo_string += lineage + ", "
                                taxo_string += rank + ")"

                                hit_string += str(index)
                                hit_string += ", "
                                hit_string += str(hd[key][h_key][i_key])
                                hit_string += ", "

                                seq = hd[key][h_key]["seq"]
                                seq_string += str(hd[key][h_key][i_key])
                                seq_string += ", " + seq
                                seq_string += ", "
                                seq_string += \
                                    str(hd[key][h_key][i_key]) + ");"
                            else:
                                index = self.__taxo_check.index(lineage)

                                hit_string += str(index + 1)
                                hit_string += ", "
                                hit_string += str(hd[key][h_key][i_key])
                                hit_string += ", "

                                seq = hd[key][h_key]["seq"]
                                seq_string += str(hd[key][h_key][i_key])
                                seq_string += ", " + seq
                                seq_string += ", "
                                seq_string += \
                                    str(hd[key][h_key][i_key]) + ");"

                hit_string += str(hit_counter) + ")"
                hit_full = hit_query + hit_string
                seq_full = seq_query + seq_string
                if taxo_string != "":
                    taxo_full = taxo_query + taxo_string
                else:
                    taxo_full = None

                self.execute_queries(hit_full, taxo_full, seq_full)

                hit_string = ""
                taxo_string = ""
                seq_string = ""
                hit_counter += 1

    def execute_queries(self, hit_query, taxo_query, seq_query):
        print(hit_query)
        self.__cursor.execute(hit_query)
        self.__cursor.execute(seq_query)
        if taxo_query is not None:
            self.__cursor.execute(taxo_query)
