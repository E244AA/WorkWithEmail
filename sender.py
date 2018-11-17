import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Sender:

    def __init__(self):
        self._HOST = None
        self._FROM = None
        self._TO = None
        self._username = None
        self._password = None
        self._subject = None
        self._message = None
        self._port = None

    def setInformation(self, HOST, port, username=None, password=None):
        self._HOST = HOST
        self._username = username
        self._password = password
        self._port = port
        self._msg = MIMEMultipart('alternative')

    def login(self):
        self._ssl = smtplib.SMTP_SSL(self._HOST, self._port)
        self._ssl.login(self._username,self._password)

    def sendMessage(self, FROM, TO, subject=None, message=None, HTML=None):
        self._TO = TO
        self._FROM = FROM
        self._message = message
        self._msg['From'] = FROM
        self._msg['To'] = TO
        if(HTML == None):
            html = '<html><body><p>' + message + '</p></body></html>'
        else:
            html = HTML
        part2 = MIMEText(html, 'html')
        self._msg['Subject'] = subject
        self._msg.attach(part2)
        self._ssl.send_message(self._msg, self._FROM, self._TO)

    def quit(self):
        self._ssl.quit()
