# Generated by Django 2.0.9 on 2019-02-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object_collector', '0018_auto_20190122_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartobject',
            name='address_ip',
            field=models.CharField(max_length=15),
        ),
    ]
