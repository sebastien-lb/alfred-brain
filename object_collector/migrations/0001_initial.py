# Generated by Django 2.0.9 on 2018-11-26 17:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmartObject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address_ip', models.CharField(max_length=15)),
                ('port', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'SmartObjects',
            },
        ),
    ]
