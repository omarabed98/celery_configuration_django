import time

from celery import shared_task


@shared_task
def send_mass_emails(recipient):
    print(recipient)
    print("Started to sleep")
    time.sleep(5)
    print("Wake up from sleep")
    return 

@shared_task
def send_scheduled_emails():
    pass
