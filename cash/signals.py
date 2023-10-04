from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Cash)
def update_model_update(sender, instance, **kwargs):
    # Check if ModelB related to this instance of ModelA exists
    try:
        model_update_instance = CashUpdate.objects.get(new_os=instance)
    except CashUpdate.DoesNotExist:
        model_update_instance = None

    # Create or update ModelB based on changes in ModelA
    if model_update_instance:
        model_update_instance.data = instance.new_os  # Update ModelB data field based on ModelA changes
        model_update_instance.save()
    else:
        CashUpdate.objects.create(cash=instance, new_os=instance.new_os)




from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import date

@receiver(pre_save, sender=Cash)
def set_date_if_checkbox_unchecked(sender, instance, **kwargs):
    if not instance.checkbox_field:
        # Checkbox is unchecked, so set the date_field to the current date.
        instance.date_field = date.today()