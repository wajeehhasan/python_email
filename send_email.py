#for simple mail use this lib
import smtplib
#to attach body to msg
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
#to attach images and text files use these libs
from email.mime.base import MIMEBase
from email import encoders

#account settings
email_sender="wajeeh.hasan322@gmail.com"
email_reciever="officialjunks@yahoo.com"
t_subject="This is test subject"
password="abc123!!22"
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

filename1="index.jpeg"
filename2="test.txt"
#create attachment and read byte by btye data of an attachment
attachment1=open(filename1,'rb') # it will read byte, rb=read byte
#now we create stream of data gathering byte and turning them into an octet stream to send to server or upload
part=MIMEBase('application','octet-stream')
#now sending payload means that octet to server in th form of payload
part.set_payload((attachment1).read())

#default encoding of file attchments so we
# need to encode our files inorder to send through attachments
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename1)
#now to attach our attachment to our message
msg.attach(part)
final_body=msg.as_string()
#making server connection
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(email_sender,password)
server.sendmail(email_sender,email_reciever,final_body)
server.close()