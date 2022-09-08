# Generated by Django 4.0.6 on 2022-09-08 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addressbook', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(verbose_name='Mark')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Mark date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('riddle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressbook.person', verbose_name='Person')),
            ],
        ),
    ]
