# Generated by Django 3.2.8 on 2021-10-24 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_contactmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmessage',
            name='subject',
        ),
    ]
