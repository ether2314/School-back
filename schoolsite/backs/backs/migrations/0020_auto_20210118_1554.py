# Generated by Django 3.0.8 on 2021-01-18 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backs', '0019_auto_20210118_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studlevel',
            old_name='Id',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='studclass',
            name='name',
        ),
    ]