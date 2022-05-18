from Bio import Entrez
import time

def inlezen(file):
    """Leest het organisme bestand in en voegt deze toe aan een lijst

    :param file: file -> Staan de organismen in van de blast resultaten
    :return: organismen -> lijst -> Staan de organismen in.
    """
    organismen = []
    open_file = open(file, "r")
    for line in open_file:
        line = line.replace("\n", "")
        organismen.append(line)
    return organismen


def taxonomy(organismen):
    """ Met behulp van Entrez wordt de lineage van elk organisme
    bepaald doormiddel van een loop.

    :param organismen: lijst -> Staan de organismen in.
    :return: lineage -> lijst -> Staat de lineage per organisme in.
    """
    lineage = []
    for n in organismen:
        print(n)
        Entrez.email = "E.Wissink1@student.han.nl"
        handle = Entrez.esearch(db="Taxonomy", term=n)
        record = Entrez.read(handle)
        term_id = record["IdList"][0]
        handle = Entrez.efetch(db="Taxonomy", id=term_id, retmode="xml")
        records = Entrez.read(handle)
        lineage.append(records[0]["Lineage"])
        print("Klaar", n)
    return lineage


def wegschrijven(lineage):
    """Schrijft de lineage weg in een bestand.

    :param lineage: lijst -> Staat de lineage per organisme in.
    :return:
    """
    with open("lineage", "w") as out_handle:
        for line in lineage:
            out_handle.write(line)
            out_handle.write("\n")


if __name__ == '__main__':
    file = "organsime"
    organismen = inlezen(file)
    lineage = taxonomy(organismen)
    wegschrijven(lineage)
