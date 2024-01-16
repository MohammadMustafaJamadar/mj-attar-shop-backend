from django.shortcuts import render
from rest_framework import viewsets
from signupapis.serializers import UserSignuSerializer
from signupapis.models import UserSignupDataModal

# Create your views here.


class UserSignupViewset(viewsets.ModelViewSet):
    queryset = UserSignupDataModal.objects.all()
    serializer_class = UserSignuSerializer
