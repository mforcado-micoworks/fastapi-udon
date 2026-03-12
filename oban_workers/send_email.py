"""
Oban worker to send emails
"""

from oban import job

@job(queue="default")
def send_email(email, subject, body):
    """
    send an email (simulated)
    """

    print(f"Email: {email}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print("Sending an email...")
