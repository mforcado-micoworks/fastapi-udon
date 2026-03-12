from oban import job

@job(queue="default")
def send_email(email, subject, body):
    print(f"Email: {email}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print("Sending an email...")