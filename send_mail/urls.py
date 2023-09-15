from django.urls import path
from .views import send_email_with_attachment
from . import views
urlpatterns = [
    path('email/send/', views.send_email_with_attachment, name='emailattachment')
]