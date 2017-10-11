from django.utils import timezone
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
import os

emailInfo = {}
emailInfo['frmEmailAddress'] = os.environ['EMAIL_HOST_USER']
emailInfo['frmEmailPassword'] = os.environ['EMAIL_HOST_PASSWORD']
emailInfo['frmEmailServer'] = os.environ['EMAIL_HOST']

def send_contact_email(sender_name, sender_email, message):

    email_content = "Name: %s\nContact: %s\nMessage: %s" % (sender_name, sender_email, message)

    msg = MIMEText(email_content, 'plain')
    msg['Subject'] = 'A message from %s' % sender_name
    msg['To'] = emailInfo['frmEmailAddress']
    frmEmail, frmEmailPassword, frmEmailServer = emailInfo['frmEmailAddress'], emailInfo['frmEmailPassword'],emailInfo['frmEmailServer']
    sentTime = str(timezone.now())

    try:
        conn = SMTP_SSL(frmEmailServer)
        conn.login(frmEmail, frmEmailPassword)
        try:
            conn.sendmail(frmEmail, frmEmail, msg.as_string())
        finally:
            conn.close()
    finally:
        return
