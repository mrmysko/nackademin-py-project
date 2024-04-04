import smtplib
from email.message import EmailMessage

from FormatMessage import format_message

# Need both smtplib to establish the connection to the mail server
# and EmailMessage to compose the mail to send.


def mail_alert(products: list):
    """mail a formatted string of product updates"""

    sender = "robin.kavenius@live.se"  # This is an alias to my stmp.login mail.
    recipient = "robin.kavenius@live.se"

    message = format_message(products, alt_format=True)

    # Create a mail object.
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = "Price-thingy updates."  # Add a timestamp here.
    email.set_content(message)

    try:
        # Establish mail-server connection.
        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
        smtp.login("orkar_-.-@hotmail.com", "yhwsscbdakztbrpw")  # Password redacted
        smtp.sendmail(sender, recipient, email.as_string())
    except smtplib.SMTPAuthenticationError:
        print("Mail error: Invalid credentials.")
    except smtplib.SMTPException:
        print("Mail error.")

    smtp.quit()


if __name__ == "__main__":
    pass
