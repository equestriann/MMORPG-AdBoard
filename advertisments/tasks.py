from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from .models import User


@shared_task
def send_test_email(user_id):
    rec = User.objects.get(id=user_id)
    rec_email = rec.email
    mail_subj = 'Мейл от MMORPG'
    message = render_to_string(
        'test_mail.html',
    )
    email = EmailMessage(
        subject=mail_subj,
        body=message,
        to=[rec_email]
    )
    email.send()

