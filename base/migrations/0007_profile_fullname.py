# Generated by Django 4.0.6 on 2022-11-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_profile_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fullName',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
