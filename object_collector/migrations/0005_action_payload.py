# Generated by Django 2.0.9 on 2018-12-03 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object_collector', '0004_auto_20181203_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='payload',
            field=models.TextField(blank=True),
        ),
    ]
