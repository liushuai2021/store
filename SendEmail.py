import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = '1798964047@qq.com' #发送者
receiver = '1798964047@qq.com'
smtpserver = 'smtp.qq.com'
username = '1798964047' #自己QQ号
password = '#自己的QQ邮箱密匙'

mail_title = '主题：这是一封测试邮件'

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = Header(mail_title, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('这是计算器测试用例的执行情况', 'plain', 'utf-8'))

# 构造附件1（附件为TXT格式的文本）
# att1 = MIMEText(open('test1.txt', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="text1.txt"'
# message.attach(att1)

# 构造附件2（附件为JPG格式的图片）
# att2 = MIMEText(open('123.jpg', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="123.jpg"'
# message.attach(att2)

# 构造附件3（附件为HTML格式的网页）
att3 = MIMEText(open('计算器的加减乘除测试报告.html', 'rb').read(), 'base64', 'utf-8')
att3["Content-Type"] = 'application/octet-stream'
# 那么接收的文件就是.bin结尾，若要正常查看，将文件后缀修改成想要的后缀即可。若是嫌麻烦不想手动修改，那么代码修改为
att3["Content-Disposition"] = 'attachment; filename="计算器的加减乘除测试报告.html"'
att3.add_header('Content-Disposition','attachment',filename='计算器的加减乘除测试报告.html')
message.attach(att3)

# smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
# smtpObj = smtplib.SMTP_SSL('smtp.qq.com',465)
smtpObj = smtplib.SMTP_SSL(smtpserver,465)
smtpObj.connect(smtpserver)
smtpObj.login(username, password)
smtpObj.sendmail(sender, receiver, message.as_string())
print("邮件发送成功！！！")
smtpObj.quit()