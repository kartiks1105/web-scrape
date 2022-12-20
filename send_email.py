import pandas as pd
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

adf = pd.read_csv("/Users/sriv.kartik/Desktop/Development/flags/country_emails.csv", index_col = False)

for var in adf['EMAIL']:
    print(adf['COUNTRY'].loc[adf['EMAIL'] == var])
    msg = MIMEMultipart()
    msg = MIMEMultipart()
    msg['From'] = 'yourEmail@mail.com' #enter user's email
    msg['To'] = var                    #emails of the recipients
    msg['Subject'] = 'ABC'             #email subject
   
    message = """
#    Dear Representative of ABC ,
   
#    The Message
   
#    Best,
   
#    Kartik"""

    
    #The same message will be sent to all email addresses
    #In the message, ABC will be replaced by the name of the country to which the email is being sent
    message = message.replace("ABC", str((adf['COUNTRY'].loc[adf['EMAIL'] == var]).item()))

    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    
   # identify ourselves to smtp gmail client
    mailserver.ehlo()
    
   # secure our email with tls encryption
    mailserver.starttls()
    
   # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login('yourEmail@mail.com', 'key')

    mailserver.sendmail('yourEmail@mail.com', var ,msg.as_string()) #var is the recipients email

    mailserver.quit()