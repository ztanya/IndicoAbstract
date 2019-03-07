import conference_class


class GetterConference(object):

    @staticmethod
    def get_conference(root):

        name_en = root[0].text
        name_ru = root[1].text
        add_info_en = root[2].text
        add_info_ru = root[3].text
        number = root[4].text
        year = root[5].text
        date_en = root[6].text
        date_ru = root[7].text
        desc_en = root[8].text
        desc_ru = root[9].text

        conference = conference_class.Conference(name_en,
                                                 name_ru,
                                                 add_info_en,
                                                 add_info_ru,
                                                 number,
                                                 year,
                                                 date_en,
                                                 date_ru,
                                                 desc_en,
                                                 desc_ru)

        return conference
