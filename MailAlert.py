import smtplib

from email.message import EmailMessage
from FormatMessage import format_message
from DBModule import Database

# Need both smtplib to establish the connection to the mail server
# and EmailMessage to compose the mail to send.


def mail_alert(products: list):
    """mail a formatted string of product updates"""

    sender = "robin.kavenius@live.se"  # This is an alias to my stmp.login mail.
    recipient = "robin.kavenius@live.se"

    # In the final version, dont do dump_db here, just add a list of products actually updated.
    message = format_message(products)

    # Create a mail object.
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = "Price-thingy updates."  # Add a timestamp here.
    email.set_content(message)

    # Establish mail-server connection.
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()

    # Using my personal outlook mail.
    smtp.login("orkar_-.-@hotmail.com", "yafsdnebhgxkbfbn")
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit()


if __name__ == "__main__":
    db = Database("price.db")

    products = db.dump_db()

    mail_alert(products)
