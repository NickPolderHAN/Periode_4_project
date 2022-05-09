from Bio.Blast import NCBIWWW, NCBIXML
import time


def blast_dictionary(sequence):
    print("Start BLAST on: ")
    result_handle = NCBIWWW.qblast("blastx", "nr", sequence, matrix_name="BLOSUM62", )

    with open("my_blastx.xml", "w") as out_handle:
        out_handle.write(result_handle.read())

    with open("my_blastx.xml", "r") as out_handle:
        blast_record = NCBIXML.parse(out_handle)
        blast_record = next(blast_record)
        print(blast_record)

        # eval_thresh = 0.04
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                print("***Alignment***")
                print("Sequence:", alignment.title)
                print("Length:", alignment.length)
                print("E value", hsp.expect)


def main(sequence_dictionary):
    sequence = "CTTCTGGTTCCCTCAAAAAATTTCGCATGCCACTCTACAAAATTTATGTAGAGTGATATACACTATTGGTAGTGCAGAAAGGAGCCGCCATGATCCGCATCCACCCCGCCAGCCGCGACCCCCAGACCCTCCTCGACCCAGAGAACTGGCGATCCGCCGCCTGGAACGGCGCCCCCATCCGCGACTGCCGCGGCTGCATCGACTGCTGCGACGACGACTGGAACCGCAGCGAACCCGAATGGCGGCGCTGCTACGGCGAACACCTGGCCGAGGACGTGCGCCACGGCGTCGCGGTCTGCCG"
    blast_dictionary(sequence)
    time.sleep(5.0)
