import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText #to attach body to msg

email_sender="wajeeh.hasan322@gmail.com"
email_reciever="officialjunks@yahoo.com"
t_subject="This is test subject"
password="uirugal123!"
t_Cc="muhammad.atiq@cyber.net.pk"
text="this email is generated through python"
msg=MIMEMultipart()
msg['Subject']=t_subject
msg['From']=email_sender
msg['To']=email_reciever
msg['Cc']=t_Cc
#now we want to attach body to this object
msg.attach(MIMEText(text,'plain')) #here plain means msg body is not some htmls but a plain text

final_body=msg.as_string() #converting whole msg to string


server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(email_sender,password)
server.sendmail(email_sender,email_reciever,final_body)
server.close()