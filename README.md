# Welcome to IndicoAbstract's documentation!
Generator of Indico's Book of Abstract.

## ***abstract_class module***

Module for storing information about Abstract class.

`class abstract_class.Abstract(title, content, authors, track)`

   Stores information about title, content, authors and track of the
   abstract.
   
## ***arabic_roman module***
Module for converting arabic numbers to roman.

`arabic_roman.arabic_roman(nums)`

   Converts arabic number to roman.

## ***conference_class module***

Module for storing information about Conference class.

`class conference_class.Conference(name_en, name_ru, add_info_en,
add_info_ru, number, year, date_en, date_ru, desc_en, desc_ru)`

   Stores information about name, number, date and year, descriprion
   and additional information about the conference.
   
## ***getter_abstract_class module***

Module for getting abstract from input xml file.

`class getter_abstract_class.GetterAbstract`

   Class for getting abstract from input XML file and CSV.

   `static get_abstract(root, i)`

   Method for getting abstract from input XML file and CSV. Returns
   object of Abstracts class.

`getter_abstract_class.bring_affiliations_to_the_same(input_affiliation, key_list)`

   Function to match current affiliations with affiliations from CSV
   file. Returns replaced affiliation if it is in CSV file and
   otherwise returns input affiliation.
   
   
## ***getter_conference_class module***

Module for getting information about the conference from input XML
file.

`class getter_conference_class.GetterConference`

   Gets information about the conference.

   `static get_conference(root)`

   Gets information about the conference from XML file's root.
   Returns object of Conference class.
   
   
## ***indicoabstractgenerator_class module***

Module for generating Book of abstracts.

`class indicoabstractgenerator_class.IndicoAbstractGenerator`

 The main class for generation of the book.
 
`generate_doc(abstracts_xmlfilename, doctpl_filename, finaldocument_filename)`

 The main function for generation of the book. Creates the final
 generated document. Includes the following steps:
 1. Parsing conference information XML file.
 2. Creating and rendering DOCX file from template for generation of two first book's pages.
 3. Saving the DOCX file as a temporary.
 4. Specifying about using styles in the generated document is the same as in the template.
 5. Parsing abstracts information XML file.
 6. Adding Abstracts class objects to list.
 7. Creating a list of all Tracks,removing duplicates.
 8. Grouping abstracts list by Tracks.
 9. Adding presentation themes (Tracks) to the final document.
 10. Creating an ordered set of all affiliations.
 11. Adding titles of the abstracts.
 12. Adding the abstracts author names with indexes of e-mails and indexes of affiliations to the final
 document.
 13. Adding author e-mails and affiliations to the final document.
 14. Saving the final generated document.
 15. Printing message about success generation and path to the generated document.

* `conferenceinfo_xmlfilename` - input path of XML file about information of the conference.
* `abstracts_xmlfilename` - input path of XML file about information of the abstracts.
* `doctpl_filename` - input path of DOCX template.
* `finaldocument_filename` - input path of DOCX generated document.



## ***main module***

Module for entering information about paths to conference and abstracts XML files,
DOCX template path and final document path.
Includes a call to the final document generation function.


## ***person_class module***

Module for storing information about Person class.

`class person_class.Person(first_name, family_name, email, affiliation, is_primary_author)`

   Stores information about first name, family name, email and
   affiliation of a person.
