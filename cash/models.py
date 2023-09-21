import uuid
from django.db import models
from django.urls import reverse
from encrypted_model_fields.fields import EncryptedCharField
from datetime import datetime


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def client_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'client_{0}/{1}'.format(instance.customer, filename)


class Cash(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.CharField(max_length=150,null=False,blank=False)
    old_os = models.CharField(max_length=50,null=True,blank=True)
    new_os = models.CharField(max_length=50,null=True,blank=True)


    
    class Meta:
        verbose_name = 'Ταμειακές'
        verbose_name_plural = 'Ταμειακές'
        ordering = ['customer']

    def __str__(self):
        return str(self.customer)


class CashUpdate(TimeStampMixin):
    cash = models.ForeignKey(Cash, on_delete=models.CASCADE)
    new_os = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.cash} - {self.new_os}"