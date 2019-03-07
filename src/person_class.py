class Person(object):

    def __init__(self, first_name, family_name, email, affiliation, is_primary_author):
        self.firstName = first_name
        self.familyName = family_name
        self.email = email
        self.affiliation = affiliation
        self.isPrimaryAuthor = is_primary_author

    # def display_info(self):
    #     print("Имя: ", self.firstName + " " + self.familyName,
    #     "\tAffiliation: ", self.affiliation + "\tE-mail: " + self.email)
