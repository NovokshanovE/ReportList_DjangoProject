# Generated by Django 5.0.6 on 2024-05-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textfiles', '0016_alter_textfile_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='group_id',
        ),
        migrations.RemoveField(
            model_name='textfile',
            name='file_id',
        ),
        migrations.AddField(
            model_name='group',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textfile',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
