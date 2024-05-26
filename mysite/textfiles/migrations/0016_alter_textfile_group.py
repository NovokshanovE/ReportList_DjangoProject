# Generated by Django 5.0.6 on 2024-05-26 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textfiles', '0015_alter_textfile_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfile',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='textfiles.group'),
        ),
    ]
