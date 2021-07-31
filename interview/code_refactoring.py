import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Protocol:
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port

class MailClient:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.SMTP = Protocol('SMTP', "smtp.gmail.com", 587)
        self.IMAP = Protocol('IMAP', "imap.gmail.com", 993)

    def set_smtp(self, host="smtp.gmail.com", port=587):
        self.SMTP = Protocol('SMTP', host, port)

    def set_imap(self, host="imap.gmail.com", port=993):
        self.IMAP = Protocol('IMAP', host, port)

    def assemble_message(self, sender, recipients, subject='', text=''):
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = ', '.join(recipients)
        message['Subject'] = subject
        message.attach(MIMEText(text))
        return message.as_string()

    def send_message(self, recipients, subject='', text=''):
        ms = smtplib.SMTP(self.SMTP.host, self.SMTP.port)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, self.assemble_message(self.login, recipients, subject=subject, text=text))
        ms.quit()

    def receive_message(self, folder="inbox", header=None):
        mail = imaplib.IMAP4_SSL(self.IMAP.host, self.IMAP.port)
        mail.login(self.login, self.password)
        mail.list()
        mail.select(folder)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message


if __name__ == '__main__':
    my_login = 'login@gmail.com'
    my_password = 'qwerty'
    mail_client = (my_login, my_password)
    mail_client.send_message(['vasya@email.com', 'petya@email.com'],
                             subject='Hello message',
                             text='Hello')
    my_message = mail_client.receive_message()











