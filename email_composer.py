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


def email_sender(sender, password, s_host, s_port, template, student_dict, subject="", audio_path=None,
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

    text = template.format(**student_dict)
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
