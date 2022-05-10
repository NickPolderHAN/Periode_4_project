from Bio.Blast import NCBIWWW, NCBIXML
import time


def blast_dictionary(key, sequence):
    print("Start BLAST on: " + key)
    result_handle = NCBIWWW.qblast("blastx", "nr", sequence,
                                   hitlist_size=10)

    with open("my_blastx.xml", "w") as out_handle:
        out_handle.write(result_handle.read())

    with open("my_blastx.xml", "r") as out_handle:
        blast_record = NCBIXML.parse(out_handle)
        blast_record = next(blast_record)
        print(blast_record)
        eval_thresh = 0.04
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                print("***Alignment***")
                print("Sequence:", alignment.title)
                print("Length:", alignment.length)
                print("E value", hsp.expect)

def main(sequence_dictionary):
    for key in sequence_dictionary:
        sequence = sequence_dictionary[key][0]
        blast_dictionary(key, sequence)
        time.sleep(20.0)