# Generated by Django 3.0.8 on 2021-01-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backs', '0017_auto_20210118_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='studclass',
            name='name',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='studclass',
            name='Id',
            field=models.CharField(help_text='100lvl', max_length=6, primary_key='True', serialize=False),
        ),
    ]
