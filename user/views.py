from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication 
from rest_framework.authtoken.views import ObtainAuthToken
from .permissions import Update_Own_Credentials
class UserLogin (ObtainAuthToken): # create tokens for users on login 
    pass
# Create your views here.
class UserViewSet (viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes=[Update_Own_Credentials]