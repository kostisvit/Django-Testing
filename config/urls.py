
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('upload_files.urls')),
    path('', include('send_mail.urls'))
]
