from django_filters import FilterSet, ChoiceFilter, CharFilter, DateFromToRangeFilter
from django_filters.widgets import DateRangeWidget
from django import forms

from .extensions import CATEGORIES

class AdsFilter(FilterSet):

    category = ChoiceFilter(
        choices = CATEGORIES,
        label = 'Категория'
    )

    author = CharFilter(
        label='Автор',
        lookup_expr='icontains',
        field_name='author__username',
        widget = forms.TextInput,
    )

    title = CharFilter(
        label='Заголовок',
        lookup_expr='icontains',
        field_name='title',
        widget=forms.TextInput,
    )

    pub_date = DateFromToRangeFilter(
        widget=DateRangeWidget(
            attrs={'type': 'date'}
        ),
        field_name='pub_date',
        label = 'Дата публикации'
    )