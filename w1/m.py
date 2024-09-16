#!/usr/bin/env python3
#////////////////////////////@

import smtplib

def send_outlook_mail():

    # Defining the SMTBLIB server object
    
    

    connection = smtplib.SMTP("smtp-mail.outlook.com", 587)
    connection.starttls()
    connection.login(user=my_eml, password=pwd)
    connection.sendmail(from_addr=my_eml, to_addrs="winiyaz@proton.me", msg="SmellPanty Howz That ")
    connection.close() 

# Calling the function
send_outlook_mail()