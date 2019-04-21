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



## ***main module***

Module for entering information about paths to conference and abstracts XML files,
DOCX template path and final document path.
Includes a call to the final document generation function.


## ***person_class module***

Module for storing information about Person class.

`class person_class.Person(first_name, family_name, email, affiliation, is_primary_author)`

   Stores information about first name, family name, email and
   affiliation of a person.
