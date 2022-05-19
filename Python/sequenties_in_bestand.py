import re
import Extract_excel_data

if __name__ == '__main__':
    excel_data_dictionary = Extract_excel_data.main()
    seq_lijst = []
    lijst_seq_per_rij = []
    for value in excel_data_dictionary.values():
        for item in value:
            if re.search('^[ATGC]+$', item):
                lijst_seq_per_rij.append(item)
            seq_lijst.append(lijst_seq_per_rij)

    with open('bestand_sequenties.txt', 'w') as output:
        output.write(str(seq_lijst))