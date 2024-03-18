from celery import shared_task
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import User, Reply
from AdBoard.settings import SITE_URL


@shared_task
def new_reply_email(reply_id):
    reply = Reply.objects.get(id=reply_id)
    ad = reply.ad

    message = render_to_string(
        'new_reply_email.html',
        {
            'ad_author': ad.author.username,
            'reply_author': reply.author.username,
            'ad_title': ad.title,
            'reply_text': reply.text[:50] + '...',
        }
    )
    email = EmailMessage(
        subject='Новый отклик!',
        body=message,
        to=[ad.author.email]
    )

    email.send()


@shared_task
def status_upd_email(reply_id):
    reply = Reply.objects.get(id=reply_id)
    ad = reply.ad

    message = render_to_string(
        'status_upd_email.html',
        {
            'reply_author': reply.author.username,
            'ad_title': ad.title
        }
    )
    email = EmailMessage(
        subject='Статус изменен!',
        body=message,
        to=[reply.author.email]
    )
    email.send()
