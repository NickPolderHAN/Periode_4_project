from Bio.Blast import NCBIWWW
import time


def blast_dictionary(key, sequence, name_counter):
    """
    Takes a sequence as input, runs this sequence through the Blast
    and then stores the Blast results in a .xml file.

    :param sequence: String -> contains a sequence.
    :param key: String -> contains the id given to that sequence.
    :param name_counter: Int -> counter to skip-
                                already aligned sequences.
    :output .xml file -> writes the alignment results to a xml file.
    """
    # runs Blast on the given sequence.
    print("Started BLAST on: " + key + " " + str(name_counter))
    result_handle = NCBIWWW.qblast("blastx", "nr", sequence,
                                   hitlist_size=10,
                                   matrix_name="BLOSUM62")

    # stores the Blast results in an .xml file.
    with open("my_blastx" + str(name_counter) + ".xml", "w") \
            as out_handle:
        out_handle.write(result_handle.read())


def get_first_reads(sequence_dict):
    """
    Function to extract the first set of reads from the sequence
    dictionary and Blast them one by one using the blast_dictionary
    function.

    :param sequence_dict: Dict -> contains the sequences of the
                                    first and second set of reads.

    """

    seq_counter = 1
    alignment_counter = 0

    # opens the file containing headers of sequences that have already
    # been aligned. (used to skip already aligned sequences)
    with open("alignment_checklist.txt", "r") as check_file:
        file_contents = check_file.read()

    # loops through the dictionary containing all sequences
    # and their corresponding headers.
    for key in sequence_dict:

        # checks if a key is in the check_file contents so that it
        # may skip sequences that have already been aligned.
        if key not in file_contents and alignment_counter <= 10:
            sequence = sequence_dict[key]
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


def get_second_reads(sequence_dict):
    """
    Function to extract the second set of reads from the sequence
    dictionary and Blast them one by one using the blast_dictionary
    function.

    :param sequence_dict: Dict -> contains the sequences of the
                                    first and second set of reads.

    """
    counter = 101

    # opens the file containing headers of sequences that have already
    # been aligned. (used to skip already aligned sequences)
    with open("alignment_checklist.txt", "r") as check_file:
        file_contents = check_file.read()

    while counter <= 200:
        seq = sequence_dict[str(counter)]
        key_name = "Read2: " + str(counter)
        if key_name not in file_contents:
            key_name = "Read2: " + str(counter)
            blast_dictionary(key_name, seq, counter)

            # adds a sequence header to the check file so that it
            # will not be aligned when the code runs again.
            with open("alignment_checklist.txt", "a") as check_file:
                check_file.write(key_name + ", as .xml file #" +
                                 str(counter) + '\n')

        counter += 1


def main(sequence_dictionary):
    # used to let the user choose the set of reads they want to align.
    command = input("Enter '1' to blast the first set of reads."
                    "\nEnter '2'"
                    "to blast the second set of reads."
                    "\nawaiting input...\n")

    # condition to check if the first set was chosen.
    if command == "1":
        # used to blast the first set of reads.
        get_first_reads(sequence_dictionary)

    # condition to check if the second set was chosen.
    elif command == "2":
        # used to blast the second set of reads.
        get_second_reads(sequence_dictionary)
