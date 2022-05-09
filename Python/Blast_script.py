from Bio.Blast import NCBIWWW, NCBIXML
import time


def blast_dictionary(key, sequence):
    time.sleep(10.0)
    print("Start BLAST on: " + key)
    result_handle = NCBIWWW.qblast("blastx", "nr", sequence,
                                   hitlist_size=10)

    return result_handle

def main(sequence_dictionary):
    for key in sequence_dictionary:
        sequence = sequence_dictionary[key][0]
        results = blast_dictionary(key, sequence)
        print(results)