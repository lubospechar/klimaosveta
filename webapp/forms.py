from django import forms
from webapp.models import Message, CourseParticipant, FinalCourseParticipant


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


class CourseParticipantForm(forms.ModelForm):
    class Meta:
        model = CourseParticipant
        fields = ['first_name', 'last_name', 'email', 'phone', 'note',]

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Jméno', 'label': ''}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Příjmení', 'label': ''}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'label': ''}),
            'phone': forms.NumberInput(attrs={'placeholder': 'Telefonní číslo', 'label': ''}),
            'note': forms.Textarea(attrs={'placeholder': 'Poznámka', 'label': ''}),
        }

class FinalCourseParticipantForm(forms.ModelForm):
    class Meta:
        model = FinalCourseParticipant
        fields = ['first_name', 'last_name', 'email', 'phone', 'note', 'day_1', 'day_2',]

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Jméno', 'label': ''}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Příjmení', 'label': ''}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'label': ''}),
            'phone': forms.NumberInput(attrs={'placeholder': 'Telefonní číslo', 'label': ''}),
            'note': forms.Textarea(attrs={'placeholder': 'Poznámka', 'label': ''}),
            'day_1': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'day_2': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
