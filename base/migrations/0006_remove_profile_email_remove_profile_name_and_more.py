# Generated by Django 4.1.3 on 2022-12-03 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_profile_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='surename',
        ),
    ]