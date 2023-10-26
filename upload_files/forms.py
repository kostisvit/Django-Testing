from django import forms
from .models import UploadedFile, MasterFile,SubFile

class FirstForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)




class MasterFileForm(forms.ModelForm):
    class Meta:
        model = MasterFile
        fields = ['customer', 'master_file']

class SubFileForm(forms.ModelForm):
    class Meta:
        model = SubFile
        fields = ['sub_file']
