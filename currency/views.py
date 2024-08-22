from django.shortcuts import render

from .tasks import send_mass_emails


def mass_email_view(request):
    recipent = 'omar.a82@yahoo.com'
    print('Received the request')
    send_mass_emails(recipient=recipent)
    print('Sent to celery')
    return render(request, "index.html")
