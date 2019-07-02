#!/usr/bin/env python3
"""Module for entering information about paths to conference and abstracts XML files,
DOCX template path and final document path.
Includes a call to the final document generation function.
"""
from os import path

from src.conference import parse_conference_xml
from src.abstracts import parse_abstracts_xml, check_abstracts_consistency, check_abstract_count_symbols
from src.generator import generate_book

if __name__ == "__main__":
    root_folder = path.dirname(path.abspath(__file__))

    # CHANGE TO THE REQUIRED VALUE
    CONFERENCEINFO_XMLFILENAME = 'xml_src/conference_info.xml'
    ABSTRACTS_XMLFILENAME = 'xml_src/Abstract_NEC2019.xml'
    DOCTPL_FILENAME = 'tpl.docx'
    CSV_FILENAME = 'matches.csv'
    FINALDOCUMENT_FILENAME = 'doc_results/book_of_abstracts.docx'

    conference = parse_conference_xml(CONFERENCEINFO_XMLFILENAME)
    abstracts = parse_abstracts_xml(ABSTRACTS_XMLFILENAME, CSV_FILENAME)

    check_abstracts_consistency(abstracts)
    check_abstract_count_symbols(abstracts)

    generate_book(conference, abstracts, DOCTPL_FILENAME, FINALDOCUMENT_FILENAME)


