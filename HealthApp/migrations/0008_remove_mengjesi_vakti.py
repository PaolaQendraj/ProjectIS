# Generated by Django 2.2.1 on 2019-05-29 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0007_auto_20190529_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mengjesi',
            name='vakti',
        ),
    ]