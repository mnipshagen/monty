import pandas as pd

# Import smtplib for the actual sending function
from smtplib import SMTP

# Import the email modules we'll need
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from base64 import b64decode


# supply rz login for smtp authentication
username = "my_rz_login"
password = "my_rz_password"

# whom the mail is from
fromaddr = f"{username}@uos.de"
# the glorious text body. Has one placeholder for the TAN
text =(
"""Hey there!

As we have already mentioned in the lecture, we would like to evaluate this course.
Since this course involves a computer anyway, we opted for the online evaluation. It takes no 10 minutes and we would really appreciate it!

To participate in the survey you need a TAN. Your TAN for this evaluation is:
{0}

With your TAN go to: http://www.lehreval.uos.de/umfragen/
There you can input your TAN and fill out the form.
You know the drill: Tick the boxes according to your opinion and leave a comment if you like!

The evaluation is open until the 30th of June (next week Saturday), but better do it now ;)
We will discuss the results in the very last lecture, so stay tuned for that.

Thanks in advance it means a lot to us!
All the best,
Mo & Antonia
""")

# Reading the csv files and bringing them together 
tans = pd.read_csv("tans.csv", header=None, names=['tan']) # lehreval csv file had no header
students = pd.read_csv("participants.csv", encoding='latin-1') # studip participants csv is in latin-1
students = students[3:].reset_index() # delete lecturer and both tutors
students = students[~(students['Nutzernamen'].isin(['cstenkamp', 'mnipshagen', 'ahain', 'rbusche']))].reset_index() # delete sneaky observers

# combine the relevant parts in a new dataframe
mail_tans = pd.DataFrame({'email': students['E-Mail'], 'tan': tans['tan']})
mail_tans = mail_tans.dropna(subset=['email']) # remove missing mails

# the network part
with SMTP("smtp-auth.uni-osnabrueck.de") as smtp:
    print(smtp.ehlo()) # check connection
    smtp.starttls() # uni smpt requires tls
    print(smtp.login(username, password)) # try to login. throws if not successful
    print(smtp.ehlo()) # check connection again. should be the same as above.

    # iterate over email and tan to send all the mails
    for idx, row in mail_tans.iterrows():
        toaddr = row['email']

        msg = MIMEMultipart() # create a new mime compliant structure
        # set header fields
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Basic Programming in Python: Evaluation"

        # attach formatted text body as plain text
        mime = MIMEText(text.format(row['tan']), 'plain')
        msg.attach(mime)

        # generate string to send
        mail_text = msg.as_string()
        # and off it goes
        smtp.sendmail(fromaddr, toaddr, mail_text)
        # spamming the console in case we want to manually check for errors. lol. as if.
        print(mail_text)
