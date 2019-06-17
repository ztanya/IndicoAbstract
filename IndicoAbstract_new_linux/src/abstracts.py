from __future__ import print_function
import csv
import xml.etree.cElementTree as ET

import lxml.etree as LXML_ET


class Abstract:
    """Stores information about title, content, authors and track of the abstract."""

    def __init__(self, title, content, authors, track):
        """Class constructor."""
        self.title = title
        self.content = content
        self.authors = authors
        self.track = track


class Person:
    """Stores information about first name, family name, email and affiliation
        of a person."""

    def __init__(self, first_name, family_name, email, affiliation, is_primary_author):
        """Class constructor."""
        self.first_name = first_name
        self.family_name = family_name
        self.email = email
        self.affiliation = affiliation
        self.is_primary_author = is_primary_author


def bring_affiliations_to_the_same(input_affiliation, key_list):
    """Function to match current affiliations with affiliations from CSV file.
    Returns replaced affiliation if it is in CSV file and otherwise
    returns input affiliation."""
    input_affiliation = input_affiliation.strip().rstrip()
    if input_affiliation in key_list.keys():
        new_affiliation = str(key_list.get(input_affiliation))
        new_affiliation = new_affiliation.replace("['", "").replace("\\n']", "")
        print("The following affiliation has been replaced: ")
        print(input_affiliation + " на " + new_affiliation + "\n")
        return new_affiliation
    print("---The affiliation \"" + input_affiliation + "\" is not in the list of standards! "
          + "Check that the affiliation is written correctly." +
          "The current version of the affiliation is saved in the generated document." + "\n")
    return input_affiliation


def create_dict_standarts(csv_file):
    """Creates a dictionary from CSV file."""
    standarts = {}
    with open(csv_file, encoding='utf-8') as f_obj:
        reader = csv.DictReader(f_obj, delimiter=':')
        for line in reader:
            key = line["old_affiliation"]
            value = line["new_affiliation"]
            standarts[key] = value
    return standarts


def parse_abstracts_xml(abstracts_xmlfilename, csv_file):
    """Method for getting abstract from input XML file and CSV.
    Returns list of all abstracts.
    """
    tree_abstracts = ET.parse(abstracts_xmlfilename)
    root_abstracts = tree_abstracts.getroot()
    doc_abstracts = LXML_ET.parse(abstracts_xmlfilename)
    count_abstracts = doc_abstracts.xpath('count(//abstract)')

    track = ""
    title = ""
    content = ""
    flag = False
    authors = []
    abstracts_list = []

    standarts = create_dict_standarts(csv_file)

    for i in range(1, int(count_abstracts) + 1):
        for child in root_abstracts[i]:
            if child.tag == "Title":
                title = child.text
                continue

            if child.tag == "Content":
                content = child.text
                continue

            if child.tag == "PrimaryAuthor":
                # bringing different affiliations to the same standard
                affiliation = bring_affiliations_to_the_same(str(child[3].text),
                                                             standarts)
                primary_author = Person(str(child[0].text),
                                        str(child[1].text),
                                        str(child[2].text),
                                        affiliation,
                                        True)
                authors.append(primary_author)
                continue

            if child.tag == "Co-Author":
                # bringing different affiliations to the same standard
                affiliation = bring_affiliations_to_the_same(str(child[3].text),
                                                             standarts)
                co_author = Person(str(child[0].text),
                                   str(child[1].text),
                                   str(child[2].text),
                                   affiliation,
                                   False)
                authors.append(co_author)
                continue

            if child.tag == "Track" and not flag:
                track = child.text
                flag = True
                continue

        abstract = Abstract(title, content, authors, track)
        abstracts_list.append(abstract)
        authors = []
        flag = False

    return abstracts_list
