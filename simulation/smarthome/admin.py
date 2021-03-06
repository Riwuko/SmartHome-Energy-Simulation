from django.contrib import admin

from .models import (Building, ChargeStateRaport, Device, DeviceRaport,
                     EnergyGenerator, EnergyReceiver, EnergyStorage, Room,
                     WeatherRaport, StorageChargingAndUsageRaport)

admin.site.register(DeviceRaport)
admin.site.register(Device)
admin.site.register(Building)
admin.site.register(EnergyStorage)
admin.site.register(EnergyReceiver)
admin.site.register(EnergyGenerator)
admin.site.register(Room)
admin.site.register(WeatherRaport)
admin.site.register(ChargeStateRaport)
admin.site.register(StorageChargingAndUsageRaport)

# Register your models here.
