from    rest_framework.response import Response
from   rest_framework.views import APIView
from . models import Contacts
from .serializers import ContactsSerializer
from   rest_framework  import status



#listing contacts being posted 
class ContactListView(APIView):
    def get(self, request):
        contacts  = Contacts.objects.all()
        serializer  = ContactsSerializer(contacts, many=True)
        return  Response(serializer.data)
    
    
# function based view to  post  a contact
class  ContactsCreateView(APIView):
       def post(self, request):
           serializer  =  ContactsSerializer(data=request.data)
           if  serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
               return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           