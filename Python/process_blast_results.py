from Bio.Blast import NCBIXML
import time


# used to retrieve the Blast results from a xml file.
class BlastParser:
    """
    BlastParser takes an amount of files and uses this amount in a for
    loop to concatenate the file_number with "my_blastx" and ".xml" to get
    the file name. After processing the files it returns them one by one.

    required parameters:
    files_amount: The amount of files named my_blast[num].xml.
    """
    def __int__(self, files_amount):
        self.__counter = 1
        self.__file_count = files_amount

    def read_xml_file(self):
        while self.__counter <= self.__file_count:
            file_name = "my_blastx" + str(self.__counter) + ".xml"
            with open(file_name, "r") as out_handle:
                time.sleep(10)
                blast_record = NCBIXML.parse(out_handle)
                blast_record = next(blast_record)
                print(blast_record)
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        print("\n")
                        print("***Alignment***")
                        print("Sequence:", alignment.title)
                        print("Length:", alignment.length)
                        print("E value", hsp.expect)
                self.__counter += 1
