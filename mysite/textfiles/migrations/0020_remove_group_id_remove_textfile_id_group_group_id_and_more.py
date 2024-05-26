# Generated by Django 5.0.6 on 2024-05-26 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textfiles', '0019_rename_filegroup_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='id',
        ),
        migrations.RemoveField(
            model_name='textfile',
            name='id',
        ),
        migrations.AddField(
            model_name='group',
            name='group_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textfile',
            name='file_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]