from rest_framework import serializers
from signupapis.models import UserSignupDataModal


class UserSignuSerializer (serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField()

    class Meta:
        model = UserSignupDataModal
        fields = "__all__"
