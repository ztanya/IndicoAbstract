"""Module for storing information about Person class."""

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

    # def display_info(self):
    #     print("Имя: ", self.firstName + " " + self.familyName,
    #     "\tAffiliation: ", self.affiliation + "\tE-mail: " + self.email)
