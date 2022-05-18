from Bio.Blast import NCBIXML


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


def main():
    pass
