import AbstractClass
from PersonClass import Person
import csv

class getterAbstract_reformatted(object):

    def getAbstract(root, i):
        global primaryAuthor
        global title
        global content
        tracky = ""
        flag = False
        authors = []

        match_affils = {}
        with open("matches.csv") as f_obj:
            reader = csv.DictReader(f_obj, delimiter=':')
            for line in reader:
                key = line["old_affiliation"]
                value = line["new_affiliation"]
                match_affils[key] = value


        child_count = 0

        abstract = AbstractClass.Abstract_reformatted()

        def bringAffilToTheSame(input_affilation, key_list):
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
                    affiliation = bringAffilToTheSame(str(root[i][j][3].text), match_affils)
                    primaryAuthor = Person(str(root[i][j][0].text), str(root[i][j][1].text),str(root[i][j][2].text),
                                               affiliation)
                    authors.append(primaryAuthor)

                if root[i][j].tag == "Co-Author":
                    # приведение разных affilations к одному стандарту
                    affiliation = bringAffilToTheSame(str(root[i][j][3].text), match_affils)
                    coAuthor = Person(str(root[i][j][0].text), str(root[i][j][1].text), str(root[i][j][2].text),
                                           affiliation)
                    authors.append(coAuthor)

                if root[i][j].tag == "Track" and not flag:
                    tracky = root[i][j].text
                    flag = True


                """if root[i][j].tag == "Speaker":
                    speaker = repr(root[i][j][0].text) + repr(root[i][j][1].text) + repr(root[i][j][2].text) + repr(root[i][j][3].text)

                if root[i][j].tag == "ContributionType":
                    contributionType = root[i][j].text"""



        abstract.title = title
        abstract.content = content
        abstract.authors = authors
        abstract.track = tracky
        # abstract.speaker = speaker
        # abstract.contributionType = contributionType

        return abstract
