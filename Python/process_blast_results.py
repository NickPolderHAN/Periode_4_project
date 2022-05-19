from Bio.Blast import NCBIXML


# used to retrieve the Blast results from a xml file.
class BlastParser:
    """
    BlastParser processes a .xml file and stores its contents
    to individual variables.

    Required Parameters:
    file -> String -> The filepath to the .xml file.
    """

    def __init__(self, file, hit_id):
        self.__file_name = file
        self.__hit_counter = 0
        self.__hit_id = hit_id
        self.__org_prot_list = []
        self.__attri_dict = {}
        self.__attribute_template = {
            "score": 0.00,
            "e_val": 0.00,
            "idpercentage": 0.00,
            "organisme": "",
            "eiwit": "",
            "accessie_code": "",
            "positives": 0.00,
            "taxonomie_id": "",
            "seq_id": 0}

        self.read_xml_file()
        print(self.__attri_dict)

    # reads the .xml file given to the init and returns its data.
    def read_xml_file(self):
        temp_dict = self.__attribute_template
        with open(self.__file_name, "r") as out_handle:
            blast_record = NCBIXML.parse(out_handle)
            blast_record = next(blast_record)

            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    self.split_organism_protein(alignment.hit_def)

                    temp_dict["score"] = float(hsp.score)
                    temp_dict["e_val"] = float(hsp.expect)
                    temp_dict["idpercentage"] = 0.00
                    temp_dict["organisme"] = self.__org_prot_list[0]
                    temp_dict["eiwit"] = self.__org_prot_list[1]
                    temp_dict["accessie_code"] = alignment.hit_id
                    temp_dict["positives"] = hsp.positives
                    temp_dict["taxonomie_id"] = ""
                    temp_dict["seq_id"] = self.__hit_id

                    # adds the temporary dictionary containing the hit data of
                    # an individual hit to the main hit data dictionary.
                    self.__hit_counter += 1
                    hit_name = "hit " + str(self.__hit_counter)
                    self.__attri_dict[hit_name] = temp_dict
                    temp_dict = {}

    def split_organism_protein(self, hit_def):
        """
        Takes the hit_def string as input and separates the Protein and
        Organism names. If multiple organism and protein combos are
        present the function gives the combos and id and appends them
        to the

        :param hit_def: String -> contains the hit_def from the
                                .xml file hit which the read_xml_file
                                function is currently processing.
        """
        # splits the different organism + protein combos
        # that are present in the hit_def String.
        hit_def_split = hit_def.split(">")
        organism_list = []
        protein_list = []
        counter = 1

        for hit_def_single in hit_def_split:
            # splits the organism and protein combos that are present
            # in the hit_def.
            def_list = hit_def_single.split("[")

            protein = def_list[0].strip()
            organism = def_list[1].replace("]", "")

            # appends the proteins and organisms to a list and
            # numbers them by giving both the same id.
            protein_list.append(protein + " (#" + str(counter) + ")")
            organism_list.append(organism + " (#" + str(counter) + ")")
            counter += 1

        # used to return the list to the read function
        self.__org_prot_list.append(organism_list)
        self.__org_prot_list.append(protein_list)
