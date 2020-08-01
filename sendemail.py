#make sure u enable gmails less secure apps option while sending the email


import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("email", "password")


#the below text format of 3 doublequotes and the backwardslash and the word Subject follewed in the immediately next line is important

message = """\
Subject: Hi this is an automated message from python

Hi , this is the automated message

	
"""
server.sendmail("from@email.com", "to@email.com", message)




