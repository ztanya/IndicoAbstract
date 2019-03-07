#!/usr/bin/env python3.7
import indicoabstractgenerator_class


if __name__ == "__main__":

    CONFERENCEINFO_XMLFILENAME = "../xml_sources/conference_info_boa.xml"
    ABSTRACTS_XMLFILENAME = "../xml_sources/Abstracts.xml"
    DOCTPL_FILENAME = "../tpl.docx"
    FINALDOCUMENT_FILENAME = "../doc_results/generated_doc_final.docx"

    GENERATOR = indicoabstractgenerator_class.IndicoAbstractGenerator
    GENERATOR.generate_doc(CONFERENCEINFO_XMLFILENAME,
                           ABSTRACTS_XMLFILENAME,
                           DOCTPL_FILENAME,
                           FINALDOCUMENT_FILENAME)
