# Generated by Django 4.0.6 on 2022-08-17 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_delete_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]