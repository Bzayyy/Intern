# Generated by Django 3.1.7 on 2021-05-02 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_auto_20210502_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisementpost',
            name='featured',
        ),
    ]
