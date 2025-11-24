# cs27-Groupwork-pt1
repository for our work
Groupe 6:Codeur Pro
group members:
CONGO Sougrinoma Anifatou(chef)
YAMEOGO Firmin
KANTIONO Diane
ZOUNGRANA Zalissa
DAKUYO Annette Alexias Prisca
NANA marc

Description for partie 1:
our project prompts the user to enter various personal and academic details (name, birth year, school, ID, etc.) using input() calls.
It calculates the student's age and key dates related to the card (delivery year, expiration, end of studies) based on the entered values.
The program then displays a formatted summary of the student card, including all entered fields and calculated values.
A boolean variable valide = True is used to indicate that the card is currently valid, and this status is shown at the end of the summary.

Description for partie 2:
The file defines two classes: Person (with attributes name, surname, birth year, and gender) and Student, which inherits from Person and adds academic-related fields (school, ID, major, academic year, parent’s name and phone number, start year, and height).
The enter_information() method prompts the user to input data using input().strip(), converts the input types (int/float), and repeats the prompt until the corresponding validator returns True.
Several validators check specific rules: minimum age (birth year), ID length, parent’s phone format/length, consistency between start year and academic year (start_year ≤ academic_year), height range (between 0.5 and 2.5 meters), and academic year being close to the current year.
There are also utility methods: calculate_age(), calculate_finish_year(), text converters (uppercase/capitalization), and display_information() which prints a formatted student profile.
The main() function creates a Student object initialized with empty values, starts the interactive input process, applies text formatting to names, and displays the student card.
