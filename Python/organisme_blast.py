from Bio.Blast import NCBIXML


def blast_inlezen(counter, organisme):
    organis = ""
    test = False
    with open("my_blastx" + str(counter) + ".xml", "r") as out_handle:
        blast_record = NCBIXML.parse(out_handle)
        blast_record = next(blast_record)
        eval_thresh = 0.04
        for alignment in blast_record.alignments:
            org = alignment.hit_def
            for letter in org:
                if letter == "[":
                    test = True
                elif letter == "]":
                    test = False
                    organisme.append(organis)
                    organis = ""
                elif test:
                    organis += letter

    counter += 1
    return counter, organisme


def main():
    counter = 1
    organisme = []
    for n in range(50):
        counter, organisme = blast_inlezen(counter, organisme)
    with open("organsime", "w") as out_handle:
        for org in organisme:
            out_handle.write(org)
            out_handle.write("\n")


main()
