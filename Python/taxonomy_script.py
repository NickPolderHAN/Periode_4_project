from Bio import Entrez


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


def nummer(organismen):
    uniek = {}
    counter = 1
    nummers_tax = []
    for o in organismen:
        if o not in uniek:
            uniek[o] = counter
            counter += 1
    for o in organismen:
        num = uniek.get(o)
        nummers_tax.append(num)
    return uniek


def taxonomy(uniek):
    """ Met behulp van Entrez wordt de lineage van elk organisme
    bepaald doormiddel van een loop.

    :param organismen: lijst -> Staan de organismen in.
    :return: lineage -> lijst -> Staat de lineage per organisme in.
    """
    organismen = uniek.keys()
    lineage = []
    rank = []
    for n in organismen:
        print(n)
        Entrez.email = "E.Wissink1@student.han.nl"
        handle = Entrez.esearch(db="Taxonomy", term=n)
        record = Entrez.read(handle)
        term_id = record["IdList"][0]
        handle = Entrez.efetch(db="Taxonomy", id=term_id, retmode="xml")
        records = Entrez.read(handle)
        lineage_string = (records[0]["Lineage"])
        rank_string = (records[0]["Rank"])
        if lineage_string not in lineage:
            lineage.append(lineage_string)
            rank.append(rank_string)
        print("Klaar", n)
    return lineage, rank


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
    uniek = nummer(organismen)
    lineage, rank = taxonomy(uniek)
    wegschrijven(lineage)
