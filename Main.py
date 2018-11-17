import sender
import email_getter

HOST = "smtp.yandex.ru"
SUBJECT = ""
TO = ""
FROM = "russian.patriot2001@yandex.ru" # - author
text = ""

username = 'user'
password = 'pass'

s = sender.Sender()

s.setInformation(HOST,465,username,password)
s.login()
s.sendMessage(FROM,TO,SUBJECT,text)
s.quit()
