import smtplib, ssl

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(sender_email, password)
connection.sendmail(
    sender_email="maxblade1232@gmail.com",
    receiver_email="nedashaik277@gmail.com",
    message="""\
               Subject: Hi there

               This message is sent from Python. The ISS is in the sky , find it"""
)