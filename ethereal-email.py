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
SMTP_PASSWORD = "password"
EMAIL_FROM = "toran.sahu@yahoo.com"
EMAIL_TO = "kanishka.ethereal@gmail.com"
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

html = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Coupon Code!</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    *,
    *::after,
    *::before {
      margin: 0;
      padding: 0;
      box-sizing: inherit;
    }

    html {
      font-size: 62.5%;
    }

    body {
      font-family: sans-serif;
      font-size: 1.6rem;
      line-height: 1.7;
      color: black;
      box-sizing: border-box;
      position: relative !important;
      padding: 2rem 1rem;
    }

    .wrapper {
      max-width: 60rem;
      margin: 0 auto;
      padding: 2rem 1rem;
    }

    .content {
      text-align: center;
      box-shadow: 0 5px 20px grey;
      background-color: #fff;
      background-image: linear-gradient(to top, rgba(252, 252, 252, 0.85), rgba(252, 252, 252, 0.2)), url('http://drive.google.com/uc?export=view&id=1a1fNGZ_2xKXR-wm6gG1_Z4Nn5F36p4Ws');
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
    }

    .content__welcome {
      height: 200px;
      background-image: linear-gradient(to right, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), url('http://drive.google.com/uc?export=view&id=12rLZ5TV0xqALlG44V2uAfE0eMVHtLbvq');
      background-color: rgba(0, 0, 0, 0.8);
      background-size: cover;
      background-position: top;
      background-repeat: no-repeat;
      position: relative !important;
    }

    .heading-primary {
      position: absolute !important;
      top: 50% !important;
      left: 50% !important;
      transform: translate(-50%, -50%) !important;
      color: white;
      font-weight: 200;
      line-height: 1.3;
      letter-spacing: .2rem;
      text-indent: .2rem;
    }

    .content__coupon-detail {
      padding: 1rem 2rem;
    }

    .heading-secondary {
      font-weight: 400;
      padding: 1rem 0;
    }

    .coupon-code {
      display: inline-block;
      font-size: 2rem;
      font-weight: 200;
      background: linear-gradient(to right, rgba(0, 0, 0, 0.8),  rgba(0, 0, 0, 0.8));
      color: orange;
      padding: .5rem 2rem;
      letter-spacing: 1rem;
      text-indent: 1rem;
    }

    .msg {
      padding: 1rem 0;
      max-width: 40rem;
      margin: 0 auto;
    }

    .content__logo-container {
      margin-bottom: 1rem;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="content wrapper">
      <div class="content__logo-container">
        <img src='https://drive.google.com/uc?export=view&id=1KPdup9MEKhZYn8-DcRrWCiySvJkB97LJ' alt="Ethereal Machines" width="80" height="80" style="width: 80px; height: 80px;">
      </div>
      <div class="content__welcome" style="position: relative !important;">
        <h1 class="heading-primary" style="
        position: absolute !important;
        top: 50% !important;
        left: 50% !important;
        transform: translate(-50%, -50%) !important;">
          Welcome to <br> Ethereal Family!
        </h1>
      </div>
      <div class="content__coupon-detail">
        <h2 class="heading-secondary">Thanks for booking your pre-order!</h2>
        <br>
        <img src='https://drive.google.com/uc?export=view&id=1ISjmQAhzMYJsJ-lHoaxaJwZZbb2r53xX' alt="Ethereal Ray" width="100"  height="100" style="width: 100px; height: 100px;">
        <p>Your coupon Code is</p>
        <p class="coupon-code">{{token}}</p>
        <p class="msg">You can use the coupon code at the time of ordering.<br> We shall notify you soon about the ensuing details.</p>
      </div>
      <div class="content__signature">
        <p><b>"Team Ethereal"</b></p>
      </div>
    </div>
  </div>
</body>
</html>
"""

def send_email():
    msg = MIMEText(html, 'html')
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
