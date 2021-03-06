import Extract_excel_data
import Blast_script
import SQL_connector as Scc
import re


def gather_sequences_from_dict(excel_data_dict):
    """
    Stores all the original sequences to a dictionary and gives
    them an id (for example: id 1 and 2 are
    corresponding reads 1 and 2.)

    :return: seq_dict -> Dict -> Dictionary containing all the
                                original sequences from the Excel
                                data dictionary.

    """
    seq_dict = {}
    list_seq_per_row = []
    counter = 0

    for value in excel_data_dict.values():
        for item in value:
            if re.search('^[ATGC]+$', item):
                list_seq_per_row.append(item)

        counter += 1
        seq_dict[str(counter)] = list_seq_per_row[0]
        seq_dict[str(counter + 100)] = list_seq_per_row[1]
        list_seq_per_row = []

    return seq_dict


if __name__ == '__main__':
    excel_data_dictionary = Extract_excel_data.main()
    sequence_dict = gather_sequences_from_dict(excel_data_dictionary)
    Blast_script.main(sequence_dict)
    # Scc.DatabaseInsert()
