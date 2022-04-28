import pandas as pd
from datetime import datetime
from random import choice
import smtplib

BIRTHDAY_LETTERS = [
    r"letter_templates/letter_1.txt",
    r"letter_templates/letter_2.txt",
    r"letter_templates/letter_3.txt"
]

def sendHappyBirthday(email, message):
    my_email = "YOUR@EMAIL.COM"
    pwd = "GEHEIM"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pwd)
        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f"Subject:Happy Birthday\n\n{message}")
        connection.close()

today = datetime.now()

birthday_df = pd.read_csv(r"birthdays.csv")
birthday_df_dict = birthday_df.to_dict(orient="records")

birthday_letter = choice(BIRTHDAY_LETTERS)

for friend in birthday_df_dict:
    if today.month == friend['month'] and today.day == friend['day']:

        with open (birthday_letter, 'r') as file:
            message = file.read()
            message = message.replace("[NAME]", friend["name"])

        sendHappyBirthday(email=friend["email"], message=message)

print("Done!")
