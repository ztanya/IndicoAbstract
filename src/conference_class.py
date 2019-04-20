"""Module for storing information about Conference class."""

class Conference:
    """Stores information about name, number, date and year,
    descriprion and additional information about the conference.
    """

    def __init__(self,
                 name_en,
                 name_ru,
                 add_info_en,
                 add_info_ru,
                 number,
                 year,
                 date_en,
                 date_ru,
                 desc_en,
                 desc_ru):
        """Class constructor."""
        self.name_en = name_en
        self.name_ru = name_ru
        self.add_info_en = add_info_en
        self.add_info_ru = add_info_ru
        self.number = number
        self.year = year
        self.date_en = date_en
        self.date_ru = date_ru
        self.desc_en = desc_en
        self.desc_ru = desc_ru
