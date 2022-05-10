from Bio.Blast import NCBIWWW, NCBIXML
import time


def blast_dictionary(key, sequence, name_counter):
    print("Start BLAST on: " + key)
    result_handle = NCBIWWW.qblast("blastx", "nr", sequence,
                                   hitlist_size=10)

    with open("my_blastx" + name_counter + ".xml", "w") as out_handle:
        out_handle.write(result_handle.read())


def main(sequence_dictionary):
    counter = 1

    for key in sequence_dictionary:
        sequence = sequence_dictionary[key][0]
        blast_dictionary(key, sequence, counter)
        time.sleep(6.0)
        counter += 1