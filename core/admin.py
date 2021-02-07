from django.contrib import admin
from core.models import Report


# Register your models here.
class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'depto', 'date', 'description')
    list_filter = ('name', 'depto', 'date',)

admin.site.register(Report, ReportAdmin)
