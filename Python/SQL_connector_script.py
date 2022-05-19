import mysql.connector
import process_blast_results
import Extract_excel_data


class DatabaseInsert:
    def __init__(self):
        # contains all the individual hit data per blast.xml file.
        self.__hit_dict = {}

        # contains all the sequences with their id.
        self.__seq_dict = {}
        self.__origin_dict = Extract_excel_data.main()

        # contains all the taxonomy data with corresponding id's
        self.__taxonomy_dict = {}

        # specifies the amount of files to be read (my_blast[num].xml)
        self.__file_amount = 98

        # calls the functions to get all the needed table data.
        print("Working.....")
        self.get_all_hits_taxonomy()
        self.get_all_sequences()

    def insert_sequence(self):
        pass

    def insert_hit(self):
        pass

    def insert_taxonomy(self):
        pass

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
            file_counter += 1
            file_name = "my_blastx" + str(file_counter) + ".xml"
            key_name = "blast hits" + str(file_counter)

            bp = process_blast_results.BlastParser(file_name, file_counter)
            hit_data = bp.get_attributes()
            self.__hit_dict[key_name] = hit_data

        print("Finished getting all hit data from .xml files.")

    def get_all_sequences(self):
        """
        Used to get all the individual sequences from the Excel data
        dictionary.

        :return: stores the sequences to the seq_dict
        """
        pass
