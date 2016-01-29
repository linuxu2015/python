#!/usr/bin/env python
import smtplib
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email import Encoders,Utils
from email.Header import Header
#author Rocky Chen 
class MailAtt():
	def __init__(self,smtp_server,from_mail,password,to_mail):
		self.server=smtp_server
		self.username=from_mail.split("@")[0]
		self.from_mail=from_mail
		self.password=password
		self.to_mail=to_mail

	def send_txt(self,filename):
		self.smtp=smtplib.SMTP()
		self.smtp.connect(self.server)
		self.smtp.login(self.username,self.password)
		self.msg=MIMEMultipart()
		self.msg['to']=self.to_mail
		self.msg['from'] =self.from_mail
		self.msg['Subject']="Convert"
		self.filename=filename+ ".txt"
		self.msg['Date']=Utils.formatdate(localtime = 1)
		content=open(self.filename.decode('utf-8'),'rb').read()
		print content
		self.att=MIMEText(content,'base64','utf-8')
		self.att['Content-Type']='application/octet-stream'
		#self.att["Content-Disposition"] = "attachment;filename="%s"" %(self.filename.encode('gb2312'))
		self.att["Content-Disposition"] = "attachment;filename=""%s" % Header(self.filename,'gb2312')
		print self.att["Content-Disposition"]
		self.msg.attach(self.att)
