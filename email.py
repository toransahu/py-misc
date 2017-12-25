#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 18:41:03 2017

@author: toran
"""

import smtplib
from email.mime.text import MIMEText


SMTP_SERVER = {'yahoo':"smtp.mail.yahoo.com",
               'gmail': "smtp.gmail.com",
               }
SMTP_PORT = {'yahoo':587,
             'gmail':587,
             }
SMTP_USERNAME = "toran.sahu@yahoo.com"
SMTP_PASSWORD = "pal060@maaES"
EMAIL_FROM = "toran.sahu@yahoo.com"
EMAIL_TO = "toransahooooo@gmail.com"
EMAIL_SUBJECT = "REMINDER:"
msg_text = """
Hello, [username]! Just wanted to send a friendly appointment
reminder for your appointment:
[Company]
Where: [companyAddress]
Time: [appointmentTime]
Company URL: [companyUrl]
Change appointment?? Add Service??
change notification preference (text msg/email)"""

def send_email():
    msg = MIMEText(msg_text)
    msg['Subject'] = EMAIL_SUBJECT + "Company - Service at appointmentTime"
    msg['From'] = EMAIL_FROM 
    msg['To'] = EMAIL_TO
    debuglevel = True
    try:
        mail = smtplib.SMTP(SMTP_SERVER['yahoo'], SMTP_PORT['yahoo'])
        mail.set_debuglevel(debuglevel)
        mail.starttls()
        mail.login(SMTP_USERNAME, SMTP_PASSWORD)
        mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    except Exception as e:
        print("Oops! Something wrong happened.", e)
    finally:
        mail.quit()

if __name__=='__main__':
    send_email()