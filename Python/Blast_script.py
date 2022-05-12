from Bio.Blast import NCBIWWW, NCBIXML
import time


def blast_dictionary(key, sequence, name_counter):
    print("Started BLAST on: " + key)
    result_handle = NCBIWWW.qblast("blastx", "nr", sequence,
                                   hitlist_size=10,
                                   matrix_name="BLOSUM62")

    with open("my_blastx" + str(name_counter) + ".xml", "w") \
            as out_handle:
        out_handle.write(result_handle.read())


def main(sequence_dictionary):
    seq_counter = 1
    alignment_counter = 0

    # opens the file containing headers of sequences that have already
    # been aligned. (used to skip already aligned sequences)
    with open("alignment_checklist.txt", "r") as check_file:
        file_contents = check_file.read()

    # loops through the dictionary containing all sequences
    # and their corresponding headers.
    for key in sequence_dictionary:

        # checks if a key is in the check_file contents so that it
        # may skip sequences that have already been aligned.
        if key not in file_contents and alignment_counter <= 20:
            sequence = sequence_dictionary[key][0]
            blast_dictionary(key, sequence, seq_counter)
            time.sleep(10.0)

            # adds a sequence header to the check file so that it
            # will not be aligned when the code runs again.
            with open("alignment_checklist.txt", "a") as check_file:
                check_file.write(key + ", as .xml file #" +
                                 str(seq_counter) + '\n')
            seq_counter += 1
            alignment_counter += 1

        else:
            seq_counter += 1
