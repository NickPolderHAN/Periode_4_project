import mysql.connector
import process_blast_results


class DatabaseInsert:
    def __init__(self, hit_data=None, seq_data=None, taxo_data=None):
        self.__hit_dict = hit_data
        self.__seq_dict = seq_data
        self.__taxonomy_dict = taxo_data

    def insert_sequence(self):
        pass

    def insert_hit(self):
        pass

    def insert_taxonomy(self):
        pass


def insert_to_database(file_amount):
    counter = 1
    hit_id_counter = 1
    file_name = "my_blastx90.xml"
    bp = process_blast_results.BlastParser(file_name, hit_id_counter)


def main():
    file_amount = 98
    insert_to_database(file_amount)
