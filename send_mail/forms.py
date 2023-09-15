# forms.py
from django import forms
from django.core.exceptions import ValidationError


def file_size(value): # add this to some file where you can import it from
    limit = 10 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')

class EmailForm(forms.Form):
    email = forms.EmailField()
    email_bcc = forms.EmailField()
    subject = forms.CharField(max_length=100)
    attachments = forms.FileField(validators=[file_size],label="Please select at least one file",widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), required=False)
    message = forms.CharField(widget = forms.Textarea)