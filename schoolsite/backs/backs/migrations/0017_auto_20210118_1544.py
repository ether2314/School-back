# Generated by Django 3.0.8 on 2021-01-18 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backs', '0016_auto_20210118_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studclass',
            name='Id',
            field=models.CharField(choices=[('100lvl', '100lvl'), ('200lvl', '200lvl'), ('300lvl', '300lvl'), ('400lvl', '400lvl'), ('500lvl', '500lvl')], max_length=6, primary_key='True', serialize=False),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='class_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backs.StudClass'),
        ),
    ]
