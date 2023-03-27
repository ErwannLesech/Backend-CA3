from django.contrib import admin

from .models import Motorcycle

# The admin.py file allows for the management of the app's data through the
# admin interface. In other words, it provides a way to interact with the data
# model in a graphical user interface. 

class MotorcycleAdmin(admin.ModelAdmin):
    # The fields attribute defines the fields that will be displayed on the
    # change list page for the model. The fieldsets attribute defines the
    # fieldsets that will be displayed on the add/change page for the model.
    fieldsets = [
        (None,               {'fields': ['motorcycle_text']}),
        ('Brand', {'fields': ['motorcycle_brand']}),
        ('Description', {'fields': ['motorcycle_description']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Motorcycle, MotorcycleAdmin)
