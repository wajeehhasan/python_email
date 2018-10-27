import smtplib

email_sender="wajeeh.hasan322@gmail.com"
email_reciever="officialjunks@yahoo.com"
password="uirugal123!"
text="this email is generated through python"
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(email_sender,password)
server.sendmail(email_sender,email_reciever,text)
server.close()