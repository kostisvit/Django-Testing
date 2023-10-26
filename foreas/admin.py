from django.contrib import admin
from .models import *
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.models import  User


class DhmosAdmin(ImportExportModelAdmin):

    list_display = ('name', 'phone', 'address', 'city', 'teamviewer', 'fax', 'email', 'is_visible')
    list_filter = ['name', 'is_visible']
    list_editable = ['is_visible']
    search_fields = ['name', ]
    actions = ['make_visible', 'make_unvisible']
    history_list_display = ["changed_fields","list_changes"]

    def make_visible(modeladmin, request, queryset):
        queryset.update(is_visible=True)
    make_visible.short_description = "Ενεργοποίηση πελάτη"

    def make_unvisible(modeladmin, request, queryset):
        queryset.update(is_visible=False)
    make_unvisible.short_description = "Απενεργοποίηση πελάτη"



class EmployeeAdmin(ImportExportModelAdmin):
    list_display = ('dhmos', 'lastname', 'firstname','tmhma', 'phone', 'email', 'is_visible')
    list_filter = ['is_visible', 'tmhma', 'dhmos']
    search_fields = ['lastname']
    actions = ['make_visible', 'make_unvisible']

    def make_visible(modeladmin, request, queryset):
        queryset.update(is_visible=True)
    make_visible.short_description = "Ενεργοποίηση υπαλλήλου"

    def make_unvisible(modeladmin, request, queryset):
        queryset.update(is_visible=False)
    make_unvisible.short_description = "Απενεργοποίηση υπαλλήλου"



class ErgasiesResource(resources.ModelResource):
    dhmos = fields.Field(column_name='Δήμος', attribute='dhmos',widget=ForeignKeyWidget(Dhmos, 'name'))
    employee = fields.Field(column_name='Υπάλληλος', attribute='employee',widget=ForeignKeyWidget(User, 'username'))
    jobtype = fields.Field(column_name='Τύπος', attribute='jobtype')
    importdate = fields.Field(column_name='Ημ. Καταχ.', attribute='importdate')
    app = fields.Field(column_name='Εφαμογή', attribute='app')
    #info = fields.Field(column_name='Εργασία', attribute='info')
    name = fields.Field(column_name='Υπάλληλος Δήμου', attribute='name')
    time = fields.Field(column_name='Χρόνος', attribute='time')

    class Meta:
        model = Ergasies
        exclude = ('text', 'ticketid')
        export_order = ('dhmos', 'importdate', 'app', 'employee','jobtype', 'info', 'name', 'time')
                        
                        

class ErgasiesAdmin(ImportExportModelAdmin):
    date_hierarchy = 'importdate'
    list_display = ('dhmos', 'importdate','app','employee','jobtype', 'info','name','time','ticketid')
    search_fields = ['dhmos', ]
    list_filter = ['employee', 'dhmos', 'jobtype', 'app']
    list_select_related = ['employee','dhmos']
    ordering = ['importdate']
    resource_class = ErgasiesResource


admin.site.register(Dhmos, DhmosAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Ergasies, ErgasiesAdmin)