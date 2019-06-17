#!/usr/bin/env python3.7
"""Module for entering information about paths to conference and abstracts XML files,
DOCX template path and final document path.
Includes a call to the final document generation function.
"""
import os
import sys
from os import path
from pprint import pprint

from src.conference import parse_conference_xml
from src.abstracts import parse_abstracts_xml
from src.generator import generate_book

if __name__ == "__main__":
    root_folder = path.dirname(path.abspath(__file__))

    # CHANGE TO THE REQUIRED VALUE
    CONFERENCEINFO_XMLFILENAME = 'xml_src\conference_info.xml'
    ABSTRACTS_XMLFILENAME = 'xml_src\Abstracts.xml'
    DOCTPL_FILENAME = 'tpl.docx'
    CSV_FILENAME = 'matches.csv'
    FINALDOCUMENT_FILENAME = 'doc_results/book_of_abstracts.docx'


    CONFERENCEINFO_XMLFILENAME = path.join(root_folder, CONFERENCEINFO_XMLFILENAME)
    sys.path.append(CONFERENCEINFO_XMLFILENAME)

    ABSTRACTS_XMLFILENAME = path.join(root_folder, ABSTRACTS_XMLFILENAME)
    sys.path.append(ABSTRACTS_XMLFILENAME)

    DOCTPL_FILENAME = path.join(root_folder, DOCTPL_FILENAME)
    sys.path.append(DOCTPL_FILENAME)

    CSV_FILENAME = path.join(root_folder, CSV_FILENAME)
    sys.path.append(CSV_FILENAME)

    FINALDOCUMENT_FILENAME = path.join(root_folder, FINALDOCUMENT_FILENAME)
    sys.path.append(FINALDOCUMENT_FILENAME)

    conference = parse_conference_xml(CONFERENCEINFO_XMLFILENAME)
    abstracts = parse_abstracts_xml(ABSTRACTS_XMLFILENAME, CSV_FILENAME)

    generate_book(conference, abstracts, DOCTPL_FILENAME, FINALDOCUMENT_FILENAME)


