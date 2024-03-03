from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db.models import TextField
from django.forms import ModelForm, ChoiceField, CharField

from .models import Ad, Reply
from .extensions import CATEGORIES


class AdsCreateForm(ModelForm):
    category = ChoiceField(
        choices=CATEGORIES,
        label='Выберите категорию',
        help_text='*Обязательное поле',
        error_messages={
            'required': 'Необходимо выбрать категорию!'
        }
    )

    title = CharField(
        min_length=1,
        label='Заголовок',
        help_text='*Обязательное поле',
        error_messages={
            'required': 'Необходимо добавить заголовок!'
        }
    )

    content = CharField(
        widget=CKEditorUploadingWidget(),
        label='Содержание объявления',
        required=False,
        help_text='*Поле может быть пустым, однако это малоэффективно :)'
    )

    class Meta:
        model = Ad
        fields = ['category',
                  'title',
                  'content']


# TODO: убрать поле author, когда будет реализована регистрация и авторизация

class ReplyCreateForm(ModelForm):
    text = TextField()

    class Meta:
        model = Reply
        fields = [
            'text'
        ]
