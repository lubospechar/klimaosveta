from django import forms
from webapp.models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Jméno', 'label': ''}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'label': ''}),
            'message': forms.Textarea(attrs={'placeholder': 'Zpráva', 'label': ''}),
        }
        labels = {
            'name': '',
            'email': '',
            'message': '',
        }
