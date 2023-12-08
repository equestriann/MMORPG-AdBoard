from django.db import models
from django.contrib.auth.models import User
from .extensions import CATEGORIES
from ckeditor.fields import RichTextField

class Ad(models.Model):
    pub_date = models.DateTimeField(
        auto_now_add=True
    )

    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=255,
        help_text='До 255 символов',
    )

    category = models.CharField(
        max_length=18,
        choices=CATEGORIES,
        default=None,
    )

    content = RichTextField(
        blank=True
    )

    class Meta:
        ordering = ['pub_date']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'{self.title}'

    def preview(self):
        return f'{self.content[:124]}...'

class Reply(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    date_sent = models.DateTimeField(
        auto_now_add=True,
    )

    ad = models.ForeignKey(
        to=Ad,
        on_delete=models.CASCADE,
    )

    text = models.TextField(
        blank=True,
    )

    is_accepted = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ['date_sent']
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'

    def __str__(self):
        return f'{self.text[:50]}...'

    def accept(self):
        self.is_accepted = True
        self.save()

    def reject(self):
        self.is_accepted = False
        self.save()