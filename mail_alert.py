###############################################
# REPO MOVED TO mrmysko/nackademin-py-project #
###############################################

import smtplib
from email.message import EmailMessage

from helper import format_message


def mail_alert(products: list) -> str:
    """
    Mail a formatted string of product updates.
    """

    sender = ""  # This is an alias to my stmp.login mail.
    recipient = ""

    message = format_message(products, alt_format=True)

    # Create a mail object.
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = "Price-thingy updates."  # Add a timestamp here.
    email.set_content(message)

    message = f"Mailing to '{recipient}'."

    try:
        # Establish mail-server connection.
        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
        smtp.login("mail", "pass")
        smtp.sendmail(sender, recipient, email.as_string())
    except smtplib.SMTPAuthenticationError:
        message = "Mail error: Invalid credentials."
    except smtplib.SMTPException:
        message = "Mail error."

    smtp.quit()

    return message


if __name__ == "__main__":
    pass
