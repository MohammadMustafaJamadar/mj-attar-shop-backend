from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user_auth.serializers import UserSignuSerializer
from user_auth.models import UserSignupDataModal
# Create your views here.


@api_view(["GET"])
def signup(request):
    if request.method == "GET":
        users = UserSignupDataModal.objects.all()
        serialzer = UserSignuSerializer(users,many=True)
        return Response(serialzer.data, status=status.HTTP_200_OK)
