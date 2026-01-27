from django import forms
from .models import Profile

class ProfileStyleForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'theme',
            'background_color',
            'button_color',
            'button_text_color',
            'font_family',
        ]

        widgets = {
            'background_color': forms.TextInput(attrs={'type': 'color'}),
            'button_color': forms.TextInput(attrs={'type': 'color'}),
            'button_text_color': forms.TextInput(attrs={'type': 'color'}),
        }
