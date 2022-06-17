import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('mohammedmusthafacbe99@gmail.com','ugjkjttsowfygqbt')
server.sendmail('mohammedmusthafacbe99@gmail.com','mohdmusthafacbe@gmail.com','mail using python code')
print("Mail Sent Successfully")