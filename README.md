# HIWI_Email

This repository contains my software to send individual personalised e-mails to a list of students. If you're a tutor or a teacher and want to communicate with your students, you may want to take a look at this software.

# Getting started

To get the software running on your machine make a git clone of the repository and check-out to your own branch. You may want to push some of your own commits and help improve the program.

# Prerequisites 

The whole program is written in Python 3. Additionally you are going to need and excel table, saved in Microsoft Excel file. The list of used modules are:

- smtplib (normally included in Python 3)
- email (normally included in Python 3)
- tkinter (optional. Just necessary in case you want to implement the code like I did in the implementation file)

All of these can easily be installed using ```pip``` from the command line.

# Implementation

The code expects a table with the following structure:

- The first column should be reserved for the last name of the student
- The second column should be reserved for the first name.
- The first two columns do not need to start at row 1.
- The first row of every column after the first two has to contain a title that will be used to define a key of a dictionary.

Each row should contain just information about one student. This information is going to be saved in a dictionary. The first two keys are given, but the rest are defined by you. Including e-mail addresses.

When your excel table is done, you can load the information of your students using the functions in ```preparation.py```

You should loop through the rows and save the individual dictionaries in a list. Finally, use the ```email_composer.py``` to send individual e-mails to all your students. You can use my ```Implementation.py``` code as an example and maybe as guide.

## Contributing

Anyone is welcome to contribute. Feel free to create your own branch of this git repository, push your commits and request pulls and merges if you feel confident your code is going to improve the functionality of the function.

## Future projects

The idea for the future of this project is to develop a GUI that can be used by less tech-savvy teachers and tutors. Integrate the GUI with its own tables.

## Author

- **Diego M. Salgado Llamas** - contact: dsalgado@students.uni-mainz.de

