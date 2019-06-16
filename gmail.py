# -*- coding: utf-8 -*-
import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

#global value
host = "smtp.gmail.com" # Gmail STMP 서버 주소.
port = "587"
htmlFileName = ".\Image\Map.html"
htmlFileName2 = ".\Image\Build.png"

senderAddr = "cjh35692@gmail.com"     # 보내는 사람 email 주소.
recipientAddr = "cjh35692@gmail.com"   # 받는 사람 email 주소.

msg = MIMEBase("multipart", "alternative")
msg['Subject'] = "Script Tour Mail "
msg['From'] = senderAddr
msg['To'] = recipientAddr

# MIME 문서를 생성합니다.
text = MIMEText("스크립트 관광지 사진")
htmlFD = open(htmlFileName, 'rb')
htmlFD2 = open(htmlFileName2, 'rb')
HtmlPart = MIMEBase(htmlFD.read(),'html', _charset = 'UTF-8' )
HtmlPart = MIMEImage(htmlFD2.read(),'png', _charset = 'UTF-8' )
htmlFD.close()
htmlFD2.close()


# 만들었던 mime을 MIMEBase에 첨부 시킨다.
msg.attach(text)
msg.attach(HtmlPart)

# 메일을 발송한다.
s = smtplib.SMTP(host,port)
#s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
s.ehlo()
s.starttls()
s.ehlo()
s.login("cjh35692@gmail.com","ans785478")
s.sendmail(senderAddr , [recipientAddr], msg.as_string())
s.close()








































