# Generated by Django 5.0.6 on 2024-05-26 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textfiles', '0018_rename_group_filegroup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FileGroup',
            new_name='Group',
        ),
    ]
