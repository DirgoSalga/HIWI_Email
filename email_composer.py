# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:21:49 2017

@author:Dirgo
"""
import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def email_sender(sender, password, s_host, s_port, template, keys_list, student_dict, subject="", audio_path=None,
                 app_path=None, image_path=None):
    """key_list is a list of the keys that are to be used from the given dictionary.
    Normally "lastname" is the only one left out."""
    """MP3, JPG, PDF supported, others must be still be tested"""

    receiver = student_dict["Email"]

    s = smtplib.SMTP(host=s_host, port=s_port)
    s.ehlo()
    s.starttls()
    s.ehlo()

    if sender.split("@")[-1] == "students.uni-mainz.de":
        s.login(sender.split("@")[0], password)
    else:
        s.login(sender, password)

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    text = template.format(*[student_dict[i] for i in keys_list])
    print(text)
    msg.attach(MIMEText(text))

    if audio_path is not None:
        audio_data = open(audio_path, "rb").read()
        aud = MIMEAudio(audio_data, name=os.path.basename(audio_path), _subtype="mp3")
        msg.attach(aud)

    if app_path is not None:
        app_data = open(app_path, "rb").read()
        app = MIMEApplication(app_data, name=os.path.basename(app_path))
        msg.attach(app)

    if image_path is not None:
        image_data = open(image_path, "rb").read()
        img = MIMEImage(image_data, name=os.path.basename(image_path))
        msg.attach(img)

    s.send_message(msg)
    s.quit()


if __name__ == "__main__":
    from tkinter import Tk
    from excel_loader import load_excel, table_template
    from tkinter.filedialog import askopenfilename

    root = Tk()
    root.withdraw()
    excel_path = askopenfilename(title="Excel file")
    list_students = [
        load_excel(excel_path, i, "B1,B2,B3,B4,Email,%-B".split(",")) for i in range(21, 23)]
    # load_excel(excel_path, i, "B1,B2,B3,B4,Email,%-B".split(",")) for i in (6, 18)]
    print(list_students)

    table = table_template(excel_path, "B1,B2,B3,B4".split(","))  # ONLY B & BP
    print(table)
    temp = ('''Hallo {0},

Wie schon während der Übung besprochen, schicke ich dir eine Übersicht deiner Noten:

%s

Gib mir Bescheid, falls deine und meine nicht übereinstimmen.

Falls das alles stimmt hast du dann bei den Übungsblättern {5}%%.

Liebe Grüße

Diego
''' % table)

    clave = input("password:\n")
    tema = input("subject:\n")
    for stud in list_students:

        if stud["Email"] == "":
            pass
        else:
            email_sender("dsalgado@students.uni-mainz.de", clave, "mail.uni-mainz.de", 587, temp,
                         "name,B1,B2,B3,B4,%-B".split(","), stud, subject=tema)
