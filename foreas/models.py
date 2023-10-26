from django.db import models
from django.urls import reverse
import datetime
from .model_choices import *
from django.db.models import Sum


def current_year():
    return datetime.date.today().year


class Dhmos(models.Model):
    name = models.CharField(max_length=100, verbose_name='Πελάτης', blank=False)
    address = models.CharField(max_length=100, verbose_name='Διεύθυνση', blank=True, default='-')
    city = models.CharField(max_length=100, verbose_name='Πόλη', blank=True, default='-')
    phone = models.CharField(max_length=100, verbose_name='Τηλέφωνο', blank=False)
    fax = models.CharField(max_length=50, verbose_name='Fax', blank=True)
    teamviewer = models.CharField(max_length=60, verbose_name='TeamViewer', blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(max_length=250, blank=True, null=True)
    info = models.TextField(max_length=1000, verbose_name='Πληροφορίες', blank=True)
    is_visible = models.BooleanField(default=False, verbose_name='Κατάσταση')

    class Meta:
        verbose_name = 'ACS Φορέας'
        verbose_name_plural = 'ACS Φορέας'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pelatis_update', args=[str(self.id)])

    def get_absolute_url_delete(self):
        return reverse('delete_pelatis', args=[str(self.id)])


class Employee(models.Model):
    dhmos = models.ForeignKey('Dhmos', on_delete=models.CASCADE, verbose_name='Πελάτης', null=True)
    firstname = models.CharField(max_length=150, verbose_name='Όνομα', null=True)
    lastname = models.CharField(max_length=150, verbose_name='Επώνυμο', null=True)
    tmhma = models.CharField(max_length=100, choices=tmhma_choice,verbose_name='Υπηρεσία', blank=True, null=True, default='-')
    phone = models.CharField(max_length=100, verbose_name='Τηλέφωνο', blank=False)
    cellphone = models.CharField(max_length=30, verbose_name='Κινητό', blank=True)
    email = models.EmailField(blank=True, null=True)
    secondary_email = models.EmailField(blank=True, null=True)
    info = models.TextField(max_length=1000, verbose_name='Πληροφορίες', blank=True)
    is_visible = models.BooleanField(default=False, verbose_name='Κατάσταση')

    class Meta:
        verbose_name = 'ACS Στοιχεία Επικοινωνίας Υπαλλήλων'
        verbose_name_plural = 'ACS Στοιχεία Επικοινωνίας Υπαλλήλων'

    def __str__(self):
        return (self.lastname) + " " + (self.firstname)

    def get_absolute_url(self):
        return reverse('epafi_update', args=[str(self.id)])

    def get_absolute_url_delete(self):
        return reverse('delete_epafi', args=[str(self.id)])


class Ergasies(models.Model):
    dhmos = models.ForeignKey('Dhmos', on_delete=models.CASCADE, verbose_name='Πελάτης', default='-')
    importdate = models.DateField(default=datetime.date.today, verbose_name='Ημ. Κατ.', db_index=True)
    app = models.CharField(max_length=100, choices=app_choice,verbose_name='Εφαρμογή', blank=True)
    jobtype = models.CharField(max_length=100, choices=job_choice,verbose_name='Τύπος Εργασίας', default='TeamViewer')
    info = models.TextField(max_length=1000, verbose_name='Περιγραφή')
    text = models.TextField(max_length=1000, verbose_name='Σημειώσεις', blank=True)
    employee = models.ForeignKey('auth.User', max_length=100, verbose_name='Υπάλληλος',on_delete=models.CASCADE, default='-')  # delete kai
    time = models.FloatField(verbose_name='Διάρκεια')
    name = models.CharField(max_length=100, verbose_name='Υπάλληλος Επικοιν.',null=True, help_text='Επώνυμο-Όνομα', blank=True)
    ticketid = models.CharField(max_length=50, verbose_name='Αίτημα OTS', blank=True)
    
    class Meta:
        indexes = [models.Index(fields=['importdate', 'employee'])]
        verbose_name = 'ACS Εργασίες Φορέα'
        verbose_name_plural = 'ACS Εργασίες Φορέα'
        ordering = ['importdate']

    def total_work_time(self):  # Ώρες εργασίας ανα χρήστη
        today = datetime.date.today()
        return Ergasies.objects.all().filter(importdate__year=today.year, employee=self.employee).aggregate(time_all=Sum('time')).get('time_all')

    def get_symbasi(self):
        return ",".join([str(p) for p in self.symbasi.all()])

    def get_absolute_url(self):
        return reverse('ergasia_update', args=[str(self.id)])
    
    def get_absolute_url_copy_paste(self):
        return reverse('ergasia_copy_paste', args=[str(self.id)])

    def get_absolute_url_delete(self):
        return reverse('delete_ergasia', args=[str(self.id)])

