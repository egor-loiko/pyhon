# Generated by Django 4.0.6 on 2022-09-08 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addressbook', '0003_mark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mark',
            old_name='riddle',
            new_name='person',
        ),
    ]
