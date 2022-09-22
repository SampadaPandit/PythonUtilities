from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import smtplib

def send(host, port, username, password, emailFrom, emailTo, subject, body, attachment=None):
    attachment = attachment or ''
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = emailFrom
    message["To"] = emailTo
    part = MIMEText(body,"html")
    message.attach(part)

    if(attachment):
        with open(attachment, "rb") as emailAttachment:
            partfile = MIMEBase("application","octet-stream")
            partfile.set_payload(emailAttachment.read())

        encoders.encode_base64(partfile)
        emailAttachmentName = Path(attachment).name
        partfile.add_header('Content-Disposition',"attachment; filename= %s" %emailAttachmentName)
        message.attach(partfile)

    try:
        server = smtplib.SMTP_SSL(host, port)
        print(server.ehlo())
        #server.starttls()
        #server.ehlo()
        print("debug1")
        print(server.login(username, password))
        print("debug2")
        print(server.sendmail(emailFrom, emailTo, message.as_string()))
        print("Email Sent")
        server.close()
    except Exception as e:
        print(e)
        
