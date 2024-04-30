from django.urls import path
from .  views  import  ContactListView,ContactsCreateView



urlpatterns = [
    
    path('contacts',ContactListView.as_view(), name='contact_list'),
    path('create/',ContactsCreateView.as_view(), name='contact_create'),
    
]
