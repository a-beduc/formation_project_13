# Generated by Django 5.2.3 on 2025-07-05 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_remove_letting_address_delete_address_delete_letting'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Profile',
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name='profile',
                    table='profiles_profile',
                ),
            ],
        ),
    ]
