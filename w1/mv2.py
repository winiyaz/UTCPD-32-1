#!/usr/bin/env python3
#////////////////////////////@

# veersion 2 of this 

import smtplib

def send_email(sender_email, sender_password, recipient_email, message):
  """Sends an email using SMTP.

  Args:
    sender_email: The sender's email address.
    sender_password: The sender's password.
    recipient_email: The recipient's email address.
    message: The message to send.

  Returns:
    True if the email was sent successfully, False otherwise.
  """
    
  try:
    connection = smtplib.SMTP("smtp-mail.outlook.com", 587)
    connection.starttls()
    connection.login(user=sender_email, password=sender_password)
    connection.sendmail(from_addr=sender_email, to_addrs=recipient_email, msg=message)
    print("Email sent successfully!")
    return True
  except smtplib.SMTPException as e:
    print("Error sending email:", e)
    return False
  finally:
    if connection:
      connection.close()

# Example usage:
my_eml = "koizx@outlook.com"
pwd = "!6m*ck4J3O60jAws54JEw"
recipient = "wiaz@proton.me"
msg = "SmellPanty"

if send_email(my_eml, pwd, recipient, msg):
  print("Email sent successfully.")
else:
  print("Failed to send email.")