# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:05:20 2018

@author:Dirgo
"""

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from preparation import load_excel, table_template, test_text
from email_composer import email_sender

if __name__ == '__main__':

    root = Tk()
    root.withdraw()
    excel_path = askopenfilename(title="Excel file")
    list_students = [
        load_excel(excel_path, i, "B1,B2,B3,B4,Email,%-B".split(",")) for i in range(21, 23)]
        # load_excel(excel_path, i, "B1,B2,B3,B4,Email,%-B".split(",")) for i in range(6, 21)]
    print(list_students)

    table = table_template(excel_path, "B1,B2,B3,B4".split(","))  # ONLY B & BP
    # print(table)
    temp = '''Hallo {name},
    
ich wollte dich nur schnell daran erinnern, dass wir morgen eine Doppelübung machen. Es wird also von 12:15 bis ungefähr 16 Uhr gehen. 
    
Liebe Grüße
    
Diego
    '''

    # print(test_text(temp, list_students[2]))
    clave = input("password:\n")
    tema = input("subject:\n")
    for stud in list_students:

        if stud["Email"] == "":
            pass
        else:
            email_sender("dsalgado@students.uni-mainz.de", clave, "mail.uni-mainz.de", 587, temp, stud, subject=tema)
