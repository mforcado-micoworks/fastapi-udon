"""
Oban worker to send emails
"""

import asyncio
from oban import job

@job(queue="default")
async def send_email(email: str):
    """
    send an email (simulated)
    """

    await asyncio.sleep(50)

    print(f"Sending: {email}")

    return True
