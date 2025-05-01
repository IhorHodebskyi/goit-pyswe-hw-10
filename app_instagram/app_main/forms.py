from django.forms import ModelForm, TextInput, DateInput, Textarea, Select
from .models import Author, Quote


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
        widgets = {
            'fullname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'born_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'born_location': TextInput(attrs={'class': 'form-control', 'placeholder': 'Born location'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['author', 'tags', 'quote']
        widgets = {
            'author': Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'tags': TextInput(attrs={'class': 'form-control', 'placeholder': 'Tags'}),
            'quote': Textarea(attrs={'class': 'form-control', 'placeholder': 'Quote'}),
        }
