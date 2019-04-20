#!/usr/bin/env python3.7
"""Module for entering information about paths to conference and abstracts XML files,
DOCX template path and final document path.
Includes a call to the final document generation function.

"""

import indicoabstractgenerator_class


if __name__ == "__main__":

    CONFERENCEINFO_XMLFILENAME = "../xml_sources/conference_info_boa.xml"
    ABSTRACTS_XMLFILENAME = "../xml_sources/Abstracts.xml"
    DOCTPL_FILENAME = "../tpl.docx"
    FINALDOCUMENT_FILENAME = "../doc_results/generated_doc_final.docx"

    GENERATOR = indicoabstractgenerator_class.IndicoAbstractGenerator
    GENERATOR.generate_doc(CONFERENCEINFO_XMLFILENAME, ABSTRACTS_XMLFILENAME,
                           DOCTPL_FILENAME, FINALDOCUMENT_FILENAME)
