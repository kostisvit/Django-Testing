
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('upload_files.urls')),
    path('', include('send_mail.urls'))
]
