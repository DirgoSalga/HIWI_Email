# HIWI_Email

This repository contains my software to send individual personalised e-mails to a list of students. If you're a tutor or a teacher and want to communicate with your students, you may want to take a look at this software.

# Getting started

To get the software running on your machine make a git clone of the repository and check-out to your own branch. You may want to push some of your own commits and help improve the program.

# Prerequisites 

The whole program is written in Python 3. Additionally you are going to need and excel table, saved in Microsoft Excel file. The list of used modules are:

- smtplib (normally included in Python 3)
- email (normally included in Python 3)
- tkinter (optional. Just necessary in case you want to implement the code like I did in the implementation file)
- Pandas (recommended to read in the csv)

All of these can easily be installed using ```pip``` from the command line.

# Implementation

You should create csv table for the points. Each row should contain just information about one student. The columns include e-mail address, name, last name, score of a given problem sheet.

You should loop through the rows of your csv table. Finally, use the ```email_composer.py``` to send individual e-mails to all your students. You can use my ```Implementation.py``` code as an example and maybe as guide.

## Contributing

Anyone is welcome to contribute. Feel free to create your own branch of this git repository, push your commits and request pulls and merges if you feel confident your code is going to improve the functionality of the function.

## Future projects

The idea for the future of this project is to develop a GUI that can be used by less tech-savvy teachers and tutors. Integrate the GUI with its own tables.

## Author

- **Diego M. Salgado Llamas** - contact: dsalgado@students.uni-mainz.de

