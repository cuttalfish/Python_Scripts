#Author: BZ
#Date: 2018-02-03
#Note: You must use Python3 to run this script!
#The applications.csv you create should have the following columns: name,email,service

import csv              # Allows to use csv library
import getpass			# Allows to take a password as an input so it doesn't appear in terminal
import smtplib			# SMTP Library


EMAIL_MSG_BODY = """
Hi {},

We're currently performing a review of accounts. We believe you're the owner of the {} account. Can you help us in answering the questions below:

- What's your favorite color?
- Are you famous?
- I love lamp

Please provide the above information via this radar and assign it back to Blake Zimmerman.

Thank you,
Blake Zimmerman
"""

with open('applications.csv') as csv_file:             # The with allows you to open the csv and not worry about closing it manually later.
    csv_file = open('applications.csv')
    csv_reader = csv.reader(csv_file, delimiter=",")   # Tells the program what the csv is using as a delimiter.
    next(csv_reader)								   # Skips the first line of the csv which typicall has the column subjects/titles.

    smtp = smtplib.SMTP('mail.apple.com', 587)		   # Sets smtp server and port
    smtp.ehlo()										   # Required for establishing a TLS connection
    smtp.starttls()									   # Starts a TLS section for the secure passing of credentials.
    smtp.ehlo()										   # Required for establishing a TLS connection
    sender_Login = input("Login: ")
    sender_Password = getpass.getpass("Password: ")    # Accepts input for password to email
    sender_Email = input("Email: ")					   # Accepts input for sender email
    smtp.login(sender_Login, sender_Password)         # Logs into email account using credentials gathered
    for row in csv_reader:							   # Iterates through each line of csv
        name, email, service = row

        msg = EMAIL_MSG_BODY.format(name, service)
        subject = "Account Review - {}".format(service)

        email_msg = "Subject: {} \n\n{}".format(subject, msg)  # Adds a subject to emails
        smtp.sendmail(sender_Email, email, email_msg)          # Sends complete emails

    smtp.quit()										  # Closes smpt connection after lop finishes
