# Generated by Django 3.0.8 on 2021-01-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backs', '0009_studclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studclass',
            name='Year',
            field=models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year'), ('Fifth Year', 'Fifth Year'), ('Final Year', 'Final Year'), ('Final Year', 'Final Year')], max_length=12),
        ),
    ]
