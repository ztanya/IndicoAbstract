from __future__ import print_function
import csv
import abstract_class
from person_class import Person


def bring_affil_to_the_same(input_affilation, key_list):
    input_affilation = input_affilation.strip().rstrip()
    if input_affilation in key_list.keys():
        new_affiliation = str(key_list.get(input_affilation))
        new_affiliation = new_affiliation.replace("['", "")
        new_affiliation = new_affiliation.replace("\\n']", "")
        print("Была заменена следующая организация: ")
        print(input_affilation + " на " + new_affiliation + "\n")
        return new_affiliation
    else:
        print("!!!Организации " + input_affilation + " нет в списке стандартов! "
              + "Проверьте правильность написания." +
              "В сгенерированном документе сохранен текущий вариант названия организации." + "\n")
        return input_affilation


class GetterAbstract(object):

    @staticmethod
    def get_abstract(root, i):
        tracky = ""
        flag = False
        authors = []

        match_affils = {}
        with open("../matches.csv") as f_obj:
            reader = csv.DictReader(f_obj, delimiter=':')
            for line in reader:
                key = line["old_affiliation"]
                value = line["new_affiliation"]
                match_affils[key] = value

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
                    affiliation = bring_affil_to_the_same(str(root[i][j][3].text), match_affils)
                    primary_author = Person(str(root[i][j][0].text), str(root[i][j][1].text), str(root[i][j][2].text),
                                            affiliation, True)
                    authors.append(primary_author)

                if root[i][j].tag == "Co-Author":
                    # приведение разных affilations к одному стандарту
                    affiliation = bring_affil_to_the_same(str(root[i][j][3].text), match_affils)
                    co_author = Person(str(root[i][j][0].text), str(root[i][j][1].text), str(root[i][j][2].text),
                                       affiliation, False)
                    authors.append(co_author)

                if root[i][j].tag == "Track" and not flag:
                    tracky = root[i][j].text
                    flag = True

                """if root[i][j].tag == "Speaker":
                    speaker = repr(root[i][j][0].text) + repr(root[i][j][1].text) + repr(root[i][j][2].text)
                    + repr(root[i][j][3].text)

                if root[i][j].tag == "ContributionType":
                    contributionType = root[i][j].text"""

        abstract = abstract_class.Abstract(title, content, authors, tracky)
        # abstract.speaker = speaker
        # abstract.contributionType = contributionType

        return abstract
