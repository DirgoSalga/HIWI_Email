# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:05:20 2018

@author:Dirgo
"""

from tkinter import Tk
from tkinter.filedialog import askopenfilename
# from preparation import load_excel, table_template, test_text
from email_composer import email_sender
import pandas as pd

if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    table_path = askopenfilename(title="Table file")
    df = pd.read_csv(table_path)

    temp = '''Hallo {Name},

Deine korrigierte Abgabe kannst du im Anhang finden. Du hast {B1}/20 Punkte erreicht.

Liebe Grüße

Diego
    '''
    mask = pd.isna(df["B1"])
    current_df = df.loc[~mask]
    clave = input("password:\n")
    tema = input("subject:\n")
    for i in range(len(current_df)):
        text = temp.format(**current_df.iloc[i])
        sender_mail = current_df.iloc[i]["Email"]
        email_sender("dsalgado@students.uni-mainz.de", sender_mail, clave, "mail.uni-mainz.de", 587, text, subject=tema,
                     app_path=r"C:\Users\dirgo\Nextcloud\Documents\HIWI\Korrigiert\{}.pdf".format(
                         sender_mail.split("@")[0]))
