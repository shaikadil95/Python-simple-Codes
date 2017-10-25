import smtplib

sender = 'xxxxx@gmail.com'
receivers = ['shaikxxxxxxx95@gmail.com','xxxxx@gmail.com']

message = """From: INTERNET WHITEBOARD<technocratsg4@gmail.com>
To: To Person <sendersmail@gmail.com>
Subject: Welcome to INTERNET WHITEBOARD

Thank you for signing up with us


"""

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('sendermail@gmail.com','Place password here')
server.sendmail(sender, receivers, message)
print ("Thanks for signing up, Check your mail for details")
