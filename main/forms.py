from .models import Station
from django.forms import ModelForm, TextInput, Textarea


class StationForm(ModelForm):
    class Meta:
        model = Station
        fields = ['title', 'station']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'station': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }