from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Jméno'}),
        label=""
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        label=""
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Zpráva'}),
        label=""
    )
