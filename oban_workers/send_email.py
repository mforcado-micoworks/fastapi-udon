"""
Oban worker to send emails
"""

from oban import job

@job(queue="default")
async def send_email(email: str):
    """
    send an email (simulated)
    """

    print(f"Sending: {email}")
