from django.contrib import admin

# Register your models here.
from webpages import models

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']



admin.site.register(models.ContactModel, ContactAdmin)