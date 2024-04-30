from django.contrib import admin
from .models import Contacts

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'listings', 'name', 'email', 'phone','contact_date')  # Customize as needed
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listings')

admin.site.register(Contacts, ContactsAdmin)
