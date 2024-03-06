from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db.models import TextField
from django import forms

from .models import Ad, Reply
from .extensions import CATEGORIES


class AdsCreateForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=CATEGORIES,
        label='Выберите категорию',
        help_text='*Обязательное поле',
        error_messages={
            'required': 'Необходимо выбрать категорию!'
        },
        widget=forms.Select(attrs={'class': 'myfield'})
    )

    title = forms.CharField(
        min_length=1,
        label='Заголовок',
        help_text='*Обязательное поле',
        error_messages={
            'required': 'Необходимо добавить заголовок!'
        },
        widget=forms.TextInput(attrs={'class': 'myfield'})
    )

    content = forms.CharField(
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


class ReplyCreateForm(forms.ModelForm):
    text = TextField()

    class Meta:
        model = Reply
        fields = [
            'text'
        ]
