
from django.contrib import admin

# Register your models here.
from .models import petOwner, petDoctor


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('username', 'yourname', 'email',
                    'contact', 'ownerImage')


admin.site.register(petOwner, OwnerAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('username','yourname', 'email',
                    'contact', 'doctorImage')


admin.site.register(petDoctor, DoctorAdmin)
