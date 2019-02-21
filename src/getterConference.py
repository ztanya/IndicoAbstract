import Conference


class getterConference(object):

    def getConference(root):
        conference = Conference.Conference()

        conference.name_en = root[0].text
        conference.name_ru = root[1].text
        conference.addInfo_en = root[2].text
        conference.addInfo_ru = root[3].text
        conference.number = root[4].text
        conference.year = root[5].text
        conference.date_en = root[6].text
        conference.date_ru = root[7].text
        conference.desc_en = root[8].text
        conference.desc_ru = root[9].text

        return conference
