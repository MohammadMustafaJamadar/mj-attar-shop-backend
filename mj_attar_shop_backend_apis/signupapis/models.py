from django.db import models

# Create your models here.


class UserSignupDataModal (models.Model):
    user_id = models.AutoField(primary_key=True)
    user_firstname = models.CharField(max_length=50, blank=False, null=False)
    user_lastname = models.CharField(max_length=50, blank=False, null=False)
    user_email = models.CharField(max_length=50, blank=False, null=False)
    user_password = models.CharField(max_length=8, blank=False, null=False)
    user_created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_firstname
