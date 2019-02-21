class Person(object):

    def __init__(self, firstName, familyName, email, affiliation, isPrimaryAuthor):
        self.firstName = firstName
        self.familyName = familyName
        self.email = email
        self.affiliation = affiliation
        self.isPrimaryAuthor = isPrimaryAuthor

    # def display_info(self):
    #     print("Имя: ", self.firstName + " " + self.familyName, "\tAffiliation: ", self.affiliation + "\tE-mail: " + self.email)
