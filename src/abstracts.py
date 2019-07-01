# -*- coding: utf-8 -*-
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
    unknown_affiliations = []

    affiliation_standarts = create_dict_standarts(csv_file)
    
    print("1. Parsing all abstracts from XML")
    for i in range(1, int(count_abstracts) + 1):
        for child in root_abstracts[i]:
            if child.tag == "Title":
                title = child.text
                continue

            if child.tag == "Content":
                content = child.text
                continue

            if child.tag == "PrimaryAuthor" or child.tag == "Co-Author":
                # Bringing different affiliations to the same standard
                affiliation = str(child[3].text).strip()
                # If affiliation is in standards - bring affiliation to standard
                if affiliation in affiliation_standarts:
                    affiliation = affiliation_standarts[affiliation]
                else:
                    unknown_affiliations.append(affiliation)


                primary_author = Person(str(child[0].text),
                                        str(child[1].text),
                                        str(child[2].text),
                                        affiliation,
                                        True if child.tag == "PrimaryAuthor" else False)
                authors.append(primary_author)
                continue

            if child.tag == "Track" and not flag:
                track = child.text
                flag = True
                continue

        abstract = Abstract(title, content, authors, track)
        abstracts_list.append(abstract)
        authors = []
        flag = False

    # Print unknown affiliations
    unknown_affiliations = list(set(unknown_affiliations))
    print("2. The following affiliations are unknown. Please add them to CSV file with standards.")
    for affiliation in unknown_affiliations:
        print(affiliation)
    print("==============================================")

    return abstracts_list
