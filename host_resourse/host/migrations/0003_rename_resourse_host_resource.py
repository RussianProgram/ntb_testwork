# Generated by Django 4.0.6 on 2022-07-07 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0002_alter_host_ip_remove_host_owners_host_owners_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='resourse',
            new_name='resource',
        ),
    ]
