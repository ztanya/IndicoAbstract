"""Module for getting abstract from input xml file."""
from __future__ import print_function
import csv
import abstract_class
from person_class import Person


def bring_affiliations_to_the_same(input_affiliation, key_list):
    """Function to match current affiliations with affiliations from CSV file.
    Returns replaced affiliation if it is in CSV file and otherwise
    returns input affiliation."""
    input_affiliation = input_affiliation.strip().rstrip()
    if input_affiliation in key_list.keys():
        new_affiliation = str(key_list.get(input_affiliation))
        new_affiliation = new_affiliation.replace("['", "")
        new_affiliation = new_affiliation.replace("\\n']", "")
        print("The following affiliation has been replaced: ")
        print(input_affiliation + " на " + new_affiliation + "\n")
        return new_affiliation
    print("!!!The affiliation " + input_affiliation + " is not in the list of standards! "
          + "Check that the affiliation is written correctly." +
          "The current version of the affiliation is saved in the generated document." + "\n")
    return input_affiliation


class GetterAbstract:
    """Class for getting abstract from input XML file and CSV."""

    @staticmethod
    def get_abstract(root, i):
        """Method for getting abstract from input XML file and CSV.
        Returns object of Abstracts class."""
        track = ""
        title = ""
        content = ""
        flag = False
        authors = []

        match_affiliations = {}
        with open("../matches.csv") as f_obj:
            reader = csv.DictReader(f_obj, delimiter=':')
            for line in reader:
                key = line["old_affiliation"]
                value = line["new_affiliation"]
                match_affiliations[key] = value

        child_count = 0

        for child in root[i]:
            child_count = child_count + 1
        if child_count > 0:
            for j in range(0, child_count - 1):
                if root[i][j].tag == "Title":
                    title = root[i][j].text

                if root[i][j].tag == "Content":
                    content = root[i][j].text

                if root[i][j].tag == "PrimaryAuthor":
                    # приведение разных affiliations к одному стандарту
                    affiliation = bring_affiliations_to_the_same(str(root[i][j][3].text),
                                                                 match_affiliations)
                    primary_author = Person(str(root[i][j][0].text),
                                            str(root[i][j][1].text),
                                            str(root[i][j][2].text),
                                            affiliation,
                                            True)
                    authors.append(primary_author)

                if root[i][j].tag == "Co-Author":
                    # приведение разных affilations к одному стандарту
                    affiliation = bring_affiliations_to_the_same(str(root[i][j][3].text),
                                                                 match_affiliations)
                    co_author = Person(str(root[i][j][0].text),
                                       str(root[i][j][1].text),
                                       str(root[i][j][2].text),
                                       affiliation,
                                       False)
                    authors.append(co_author)

                if root[i][j].tag == "Track" and not flag:
                    track = root[i][j].text
                    flag = True

                # if root[i][j].tag == "Speaker":
                #    speaker = repr(root[i][j][0].text) +
                #    repr(root[i][j][1].text) +
                #    repr(root[i][j][2].text) +
                #    repr(root[i][j][3].text)

                # if root[i][j].tag == "ContributionType":
                #    contributionType = root[i][j].text

        abstract = abstract_class.Abstract(title, content, authors, track)

        return abstract
