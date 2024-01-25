from user_auth.models import UserSignupDataModal


def check_user_exists(user_email):
    return UserSignupDataModal.objects.filter(
        user_email=user_email
    ).exists()


if __name__ == "__main__":

    check_user_exists()
