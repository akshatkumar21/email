import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS='akshatkumar628@gmail.com'
EMAIL_PASSWORD='shockwave628'
build=2
b=str(build)
msg=EmailMessage()
msg['Subject']='Grab Dinner this weekend?'
msg['From']=EMAIL_ADDRESS
msg['To']='akshatkumar628@gmail.com'
msg.set_content('this is a number /n b')

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465 ) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    smtp.send_message(msg)