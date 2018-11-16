import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = "smtp.yandex.ru"
SUBJECT = "Test email from Python"
TO = "russian.patriot2001@yandex.ru"
FROM = "russian.patriot2001@yandex.ru"
text = "Python 3.4 rules them all!"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Nice"
msg['From'] = FROM
msg['To'] = TO

html = '<html><body><p>' + text + '</p></body></html>'
part2 = MIMEText(html, 'html')

msg.attach(part2)

username = "username"
password = "password"

s = smtplib.SMTP_SSL('smtp.yandex.ru',465)
s.login(username,password)
s.send_message(msg,FROM,TO)
s.quit()
