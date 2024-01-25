from rest_framework import serializers
from user_auth.models import UserSignupDataModal


# User-Signup Serializer 
class UserSignuSerializer (serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField()

    class Meta:
        model = UserSignupDataModal
        fields = "__all__"
