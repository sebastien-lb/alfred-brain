# Generated by Django 2.0.9 on 2018-12-03 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object_collector', '0003_auto_20181203_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasource',
            name='entrypoint',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='endpoint',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]