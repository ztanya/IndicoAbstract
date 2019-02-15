from PersonClass import Person
class PrimaryAuthor(Person):
    def __init__(self, firstName, familyName, email, affiliation):
        super().__init__(firstName, familyName, email, affiliation)