# Generated by Django 5.0.1 on 2024-01-25 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersignupdatamodal',
            name='user_password',
            field=models.CharField(max_length=20),
        ),
    ]
