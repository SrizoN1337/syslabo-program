# Generated by Django 5.0.7 on 2024-07-17 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgchart', '0003_remove_sysuser_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sysuser',
            old_name='falied_login',
            new_name='failed_login',
        ),
        migrations.RemoveField(
            model_name='sysuser',
            name='calendar',
        ),
    ]
