from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import *

class HomeView(TemplateView):
    template_name = "home.html"



    
    
def upload_files(request):
    if request.method == 'POST':
        form = FirstForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_files')

    else:
        form = FirstForm()

    files = UploadedFile.objects.all()

    return render(request, 'files.html', {'form': form, 'files': files})