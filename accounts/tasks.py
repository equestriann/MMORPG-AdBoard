from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .extensions import create_actication_code
from .models import Code, User


@shared_task
def send_activation_code(user_id):
    cur_user = User.objects.get(id=user_id)
    act_code = create_actication_code()
    Code.objects.create(user=cur_user, code=act_code)

    message = render_to_string(
        template_name='account_activation_email.html',
        context={
            'code': act_code,
            'username': cur_user.username
        },
    )
    email = EmailMessage(
        subject='Активация аккаунта на популярном MMORPG',
        body=message,
        to=[cur_user.email]
    )
    email.send()
