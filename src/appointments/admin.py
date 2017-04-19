from django.contrib import admin
from .models import Doctor, Specialization, Appointment

# Register your models here.


class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class DoctorAdmin(admin.ModelAdmin):
    list_filter = ('specialization',)
    list_display = ('full_name', 'specialization')
    search_fields = ('full_name', 'specialization__name')


class AppointmentAdmin(admin.ModelAdmin):
    list_filter = ('date', 'doctor', 'doctor__specialization')
    list_display = ('full_name', 'doctor', 'date')
    search_fields = ('full_name',)


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Appointment, AppointmentAdmin)
