import smtplib
import ssl
from email.message import EmailMessage

def sendMail(USER, PASSWORD, RECIPIENTS, SUBJECT, BODY):
    try:
        msg = EmailMessage()
        msg['From'] = USER
        msg['To'] = RECIPIENTS
        msg['subject'] = SUBJECT
        msg.set_content(BODY)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:

            smtp.login(USER, PASSWORD)
            smtp.sendmail(USER, RECIPIENTS, msg.as_string())
    except:
        return 