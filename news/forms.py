from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'announcment', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article\'s title'
            }),

            'announcment': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article\'s announcement'
            }),

            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publication\'s date'
            }),

            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article\'s text'
            }),

        }
