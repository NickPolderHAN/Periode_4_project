from Bio.Blast import NCBIXML


# used to retrieve the Blast results from a xml file.
class BlastParser:
    """
    BlastParser processes a .xml file and stores its contents
    to individual variables.

    Required Parameters:
    file -> String -> The filepath to the .xml file.
    """
    def __init__(self, file):
        self.__file_name = file
        self.__hit_counter = 1
        self.__attribute_dictionary = {}
        self.__attribute_template = {
            "score": 0.00,
            "e_val": 0.00,
            "idpercentage": 0.00,
            "organisme": "",
            "eiwit": "",
            "accessie_code": "",
            "positives": 0.00,
            "seq_header": "",
            "taxonomie_id": ""}

        self.read_xml_file()
        print(self.__attribute_dictionary)

    # reads the xml files and returns its attributes.
    def read_xml_file(self):
        temp_dict = self.__attribute_template
        with open(self.__file_name, "r") as out_handle:
            blast_record = NCBIXML.parse(out_handle)
            blast_record = next(blast_record)

            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    temp_dict["score"] = float(hsp.score)
                    temp_dict["e_val"] = float(hsp.expect)
                    temp_dict["idpercentage"] = ""
                    temp_dict["organisme"] = ""
                    temp_dict["eiwit"] = ""
                    temp_dict["accessie_code"] = alignment.hit_id
                    temp_dict["positives"] = 0
                    temp_dict["seq_header"] = alignment.title
                    temp_dict["taxonomie_id"] = ""

        # adds the temporary dictionary containing the hit data of
        # an individual hit to the main hit data dictionary.
        hit_name = "hit " + str(self.__hit_counter)
        self.__attribute_dictionary[hit_name] = temp_dict
        self.__hit_counter += 1
