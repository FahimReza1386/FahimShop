# Generated by Django 5.0.4 on 2024-06-26 14:10

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_admins'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modifiesd', models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User)),
                ('Phone', models.CharField(blank=True, default='', max_length=11)),
                ('address1', models.CharField(blank=True, default='', max_length=250)),
                ('address2', models.CharField(blank=True, default='', max_length=250)),
                ('city', models.CharField(blank=True, default='', max_length=250)),
                ('state', models.CharField(blank=True, default='', max_length=250)),
                ('zipcode', models.CharField(blank=True, default='', max_length=250)),
                ('country', models.CharField(blank=True, default='', max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]