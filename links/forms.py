from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['title', 'url', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full border rounded px-3 py-2'
            }),
            'url': forms.URLInput(attrs={
                'class': 'w-full border rounded px-3 py-2'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'mr-2'
            }),
        }
