from django.urls import path
from .views import HomeView,upload_files

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cash/cash-new',upload_files, name='cash-new'),
]