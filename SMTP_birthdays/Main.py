import smtplib
import datetime
import random


with open(file="quotes.txt") as fp:
    all_quotes = fp.readlines()
    quote = random.choice(all_quotes)

print(quote)

my_email= "devrumaan@gmail.com"
pwd="inpocaobalrdtvpj"

# find out the current day

current_day = datetime.datetime.now()

day = current_day.day
month = current_day.month
year = current_day.year

print(day)
#check if the current day is monday
if day==18:
    #send mail if condition is met
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pwd)
        connection.sendmail(from_addr=my_email, to_addrs="maxblade1232@gmail.com", msg=f"subject: Motivational Quotes\n\n{quote}")
        connection.close()


