# forms.py
from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    attachments = forms.FileField(label="Please select at least one file",widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), required=False)
    message = forms.CharField(widget = forms.Textarea)