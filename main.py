import smtplib
import random

with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)


my_email = EMAIL
my_password = PASSWORD
message = f"""From: Abdurrahman <{my_email}>
To: _ <{email_to}>
Subject: GOOD DAY

{quote}.
"""

connection = smtplib.SMTP_SSL("smtp.gmail.com")
connection.login(my_email, my_password)
connection.sendmail(from_addr=my_email, to_addrs={email_to}, msg=message)
connection.close()
