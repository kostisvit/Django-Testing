from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import *
from .models import MasterFile, SubFile

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



from .forms import MasterFileForm, SubFileForm

def upload_master_file(request):
    if request.method == 'POST':
        master_form = MasterFileForm(request.POST, request.FILES)
        sub_form = SubFileForm(request.POST, request.FILES)

        if master_form.is_valid() and sub_form.is_valid():
            master = master_form.save()
            sub_file = sub_form.save(commit=False)
            sub_file.master_file = master
            sub_file.save()
            return redirect('/')  # Create a success page
    else:
        master_form = MasterFileForm()
        sub_form = SubFileForm()
    
    return render(request, 'home.html', {'master_form': master_form, 'sub_form': sub_form})

def upload_success(request):
    return render(request, 'cash.html')




from django.shortcuts import render
from .models import MasterFile, SubFile

def custom_listview(request):
    model1_data = MasterFile.objects.all()
    model2_data = SubFile.objects.all()

    context = {
        'model1_data': model1_data,
        'model2_data': model2_data,
    }

    return render(request, 'files.html', context)