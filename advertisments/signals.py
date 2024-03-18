from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .tasks import status_upd_email, new_reply_email
from .models import Reply


@receiver(post_save, sender=Reply)
def new_reply_signal(instance, created, **kwargs):
    if created:
        reply_id = Reply.objects.get(id=instance.id).id
        new_reply_email.delay(reply_id)


@receiver(pre_save, sender=Reply)
def status_upd_signal(instance, **kwargs):
    pre_state = Reply.objects.get(id=instance.id)

    if not pre_state.is_accepted and instance.is_accepted:
        status_upd_email.delay(instance.id)

