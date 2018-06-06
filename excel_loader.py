# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:36:37 2017

These functions take a table of excel containing the first name, the last name, the grades of each exercise sheet and
creates a more useful dictionary for each student (row-wise).

@author:Dirgo
"""
import xlrd


def load_excel(filepath, row, ubung_keys):
    """rows determine which students are to be extracted from the table, with the same number as in excel"""
    """ubung_keys is a list of titles of the desired column excluding name and last name.
        The possible values in the list are B#, BP#, G-B, G-BP, Zulassung and Email"""
    rowx = row - 1
    book = xlrd.open_workbook(filepath)
    sheet = book.sheet_by_index(0)

    # Define column indexes, for the sheet numbers a dictionary
    name = 1  # Number of the column that contains all names
    lastname = 0  # Number of the column that contains all last names

    dicc_cols = dict()
    for i in range(2, sheet.ncols):
        # {k:v}={sheet_number(str):index(int)}
        dicc_cols[sheet.cell_value(0, i)] = i
    result = dict()
    result["name"] = sheet.cell_value(rowx, name).split(" ")[0]  # First name
    result["lastname"] = sheet.cell_value(rowx, lastname)
    for key in ubung_keys:
        col_index = dicc_cols[key]
        result[key] = sheet.cell_value(rowx, col_index)
    return result


def table_template(filepath, keylist):
    scores = load_excel(filepath, 2, keylist)  # Gets maximal scores
    table_str = ""
    for key in keylist:
        if key[0] == "B":
            table_str += "%s: {%s} / %.1f\n\n" % (key, key, scores[key])
        else:
            table_str += "%s: {%s} / %.1f\t" % (key, key, scores[key])
    return table_str


if __name__ == "__main__":
    # excel_path = "D:/Dirgo/Documents/HIWI/Noten.xlsx"
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    root = Tk()
    root.withdraw()
    excel_path = askopenfilename()
    print(load_excel(excel_path, 9, "B1,B2,B3,%-B".split(",")))
    print(table_template(excel_path, "B1,B2,B3,B4".split(",")))
