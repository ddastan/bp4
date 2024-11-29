from django.contrib import admin

from MobileDevices.models import Device, Category, Feature

# Register your models here.
admin.site.register(Device)
admin.site.register(Category)
admin.site.register(Feature)