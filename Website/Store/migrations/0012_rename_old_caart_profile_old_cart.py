# Generated by Django 5.0.4 on 2024-07-02 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0011_remove_profile_old_caart2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='old_caart',
            new_name='old_cart',
        ),
    ]