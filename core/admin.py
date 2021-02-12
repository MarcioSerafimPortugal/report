from django.contrib import admin
from core.models import Report, Department4


# Register your models here.
class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'depto', 'date', 'description')
    list_filter = ('name', 'depto', 'date',)


class Department4Admin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_filter = ('name', 'date',)


admin.site.register(Report, ReportAdmin)
admin.site.register(Department4, Department4Admin)
