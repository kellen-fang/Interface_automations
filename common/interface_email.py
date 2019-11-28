# coding: utf-8


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common import interface_log


# 封装发送邮件的方法
class SendEmail:

	# 初始化
	def __init__(self):
		global send_user
		global email_host
		global password

		email_host = "smtp.163.com"
		send_user = "fangxiaoqi115@163.com"
		password = "fangdijiao115@"

	# 邮件内容
	def send_mail(self,user_list,sub,content):

		user = "kellen"+"<"+ send_user+">"
		message = MIMEMultipart()
		message['Subject'] = sub
		message['From'] = user
		message['To'] = ";".join(user_list)
		# 邮件正文内容
		message.attach(MIMEText(content, 'plain', 'utf-8'))
		try:
			# 构造附件测试报告文件
			att1 = MIMEText(open("../report/接口测试报告.html", "rb").read(), 'html', 'utf-8')
			att1["Content-Type"] = 'application/octet-stream'
			# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
			att1.add_header('Content-Disposition', 'attachment', filename="接口测试报告.html")
			message.attach(att1)
		except Exception as e:
			interface_log.create_mylog().error("构造附件测试报告文件错误: %s" % e)

		# try:
		# 	# 构造附件log.log日志文件
		# 	att3 = MIMEText(open("../log/log.log", "rb").read(), 'base64', 'utf-8')
		# 	att3["Content-Type"] = 'application/octet-stream'
		# 	# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
		# 	att3.add_header('Content-Disposition', 'attachment', filename="log.txt")
		# 	message.attach(att3)
		# except Exception as e:
		# 	interface_log.create_mylog().error("构造附件log.log日志文件错误: %s" % e)

		try:
			'''构造附件err.log日志文件'''
			att2 = MIMEText(open("../log/err.log", "rb").read(), 'base64', 'utf-8')
			att2["Content-Type"] = 'application/octet-stream'
			# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
			att2.add_header('Content-Disposition', 'attachment', filename="err.txt")
			message.attach(att2)
		except Exception as e:
			interface_log.create_mylog().error("构造附件err.log日志文件错误: %s" % e)

		try:
			# 构造附件Excel测试用例文件
			att4 = MIMEText(open("../data/data.xlsx", "rb").read(), 'base64', 'utf-8')
			att4["Content-Type"] = 'application/octet-stream'
			# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
			att4.add_header('Content-Disposition', 'attachment', filename="接口测试用例.xlsx")
			message.attach(att4)
		except Exception as e:
			interface_log.create_mylog().error("构造附件附件Excel测试用例错误: %s" % e)

		try:
			# 邮箱服务连接
			server = smtplib.SMTP()
			server.connect(email_host)
			server.login(send_user,password)
			server.sendmail(user,user_list,message.as_string())
			server.close()
		except Exception as e:
			interface_log.create_mylog().error("邮箱服务连接失败: %s" % e)

	# 发送邮件
	def send_main(self):
		try:
			user_list = ['fangdijiao@ah-fuli.com']
			sub = "接口自动化测试报告"
			content = "@all: \n\t本次接口测试结果见附件测试报告及测试日志!\n "
			self.send_mail(user_list,sub,content)
		except Exception as e:
			interface_log.create_mylog().error("邮件发送失败: % s" % e)

if __name__ == '__main__':
	sen = SendEmail()
	sen.send_main()