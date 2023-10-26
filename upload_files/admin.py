from django.contrib import admin
from .models import Cash,UploadedFile,Customer,MasterFile,SubFile

admin.site.register(Cash)
admin.site.register(UploadedFile)
admin.site.register(Customer)
admin.site.register(MasterFile)
admin.site.register(SubFile)