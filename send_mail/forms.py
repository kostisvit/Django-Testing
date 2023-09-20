# forms.py
from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.helper import FormHelper

def file_size(value): # add this to some file where you can import it from
    limit = 10 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')

class EmailForm(forms.Form):
    email = forms.EmailField(label='Προς')
    bcc = forms.CharField(label='Κοινοποίηση', widget=forms.TextInput(attrs={'placeholder': 'Οι διευθύνσεις χωρίζονται με κόμμα'}),required=False)
    subject = forms.CharField(label='Θέμα',max_length=100)
    attachments = forms.FileField(validators=[file_size],label="Επιλέξτε αρχείο",widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), required=False)
    message = forms.CharField(label='Μήνυμα',widget = forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('email', css_class='form-control'),
            Field('subject', css_class='form-control'),
            Field('bcc', css_class='form-control'),
            Field('attachments', css_class='form-control'),
            Field('message', css_class='form-control'),
            Submit('submit', 'Send Email', css_class='btn btn-primary')
        )
    