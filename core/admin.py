from django.contrib import admin
from core.models import Report, Department4


#Register your models here.
class ReportAdmin(admin.ModelAdmin):
    list_display = ('complete_name', 'depto', 'data_customizada', 'description')
    search_fields = ('complete_name', 'depto', 'date', 'description')
    list_filter = ('user', 'depto', 'date',)
    exclude = ('user',)

    def get_queryset(self, request):
        qs = super(ReportAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def complete_name(self, obj):
        return obj.user.get_full_name()

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def custom_data(self, obj):
        return obj.date.strftime("%d-%m-%Y")

class Department4Admin(admin.ModelAdmin):
    list_display = ('complete_name', 'date')
    list_filter = ('user', 'date',)
    exclude = ('user',)

    def get_queryset(self, request):
        qs = super(Department4Admin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def complete_name(self, obj):
        return obj.user.get_full_name()

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def custom_date(self, obj):
        return obj.date.strftime("%d-%m-%Y")


admin.site.register(Report, ReportAdmin)
admin.site.register(Department4, Department4Admin)
