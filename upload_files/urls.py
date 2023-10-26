from django.urls import path
from .views import HomeView,upload_files
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('files/', views.custom_listview, name='file'),
    path('upload/', views.upload_master_file, name='upload_master_file'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('cash/cash-new',upload_files, name='cash-new'),
]