import uuid
from django.db import models
from encrypted_model_fields.fields import EncryptedCharField
from datetime import datetime
from .validators import validate_file_extension

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
    cash_model = models.CharField(max_length=50,null=False,blank=False)
    cash_number = models.CharField(max_length=50,null=False,blank=False)
    register_date = models.DateField(null=True,blank=True)
    old_os = models.CharField(max_length=50,null=True,blank=True)
    new_os = models.CharField(max_length=50,null=True,blank=True)
    update_date = models.DateField(null=True,blank=True)
    aes_key = EncryptedCharField(max_length=150,null=True, blank=True)
    status = models.BooleanField(default=True, blank=True,null=True)
    info = models.TextField(blank=True,null=True)
    

    
    class Meta:
        verbose_name = 'Ταμειακές'
        verbose_name_plural = 'Ταμειακές'
        ordering = ['customer']



class UploadedFile(models.Model):
    customer = models.ForeignKey(Cash,on_delete=models.CASCADE)
    file = models.FileField(upload_to=client_directory_path,validators=[validate_file_extension],blank=True,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.name)


class MasterFile(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    master_file = models.FileField(upload_to='master_files/')

class SubFile(models.Model):
    master_file = models.ForeignKey(MasterFile, on_delete=models.CASCADE)
    sub_file = models.FileField(upload_to='sub_files/')
