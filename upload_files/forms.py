from django import forms
from .models import UploadedFile

class FirstForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)
