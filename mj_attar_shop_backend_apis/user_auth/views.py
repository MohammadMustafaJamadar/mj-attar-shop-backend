from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user_auth.serializers import UserSignuSerializer
from user_auth.validations import check_user_exists


@api_view(["POST"])
def signup(request):

    try:
        if request.method == "POST":
            user_email = request.data.get("user_email")
            user_data = request.data

            is_user_exists = check_user_exists(user_email)

            if is_user_exists:
                return Response({"massage": "User already exists!"}, status=status.HTTP_409_CONFLICT)

            else:
                serializer = UserSignuSerializer(data=user_data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"massage": "User created successfully."}, status=status.HTTP_200_OK)
                else:
                    return Response({"massage": "Invalid user details."}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
