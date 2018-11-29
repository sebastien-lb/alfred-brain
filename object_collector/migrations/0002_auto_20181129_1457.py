# Generated by Django 2.0.9 on 2018-11-29 14:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('object_collector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('command', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Actions',
            },
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('endpoint', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'DataSources',
            },
        ),
        migrations.CreateModel(
            name='DataSourceType',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'DataSourceTypes',
            },
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'DataTypes',
            },
        ),
        migrations.AlterField(
            model_name='smartobject',
            name='address_ip',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(code='ip invalid', message='You must enter a valid ip address', regex='^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')]),
        ),
        migrations.AlterField(
            model_name='smartobject',
            name='port',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(code='port invalid', message='You must enter a valid port between 0 and 65535', regex='^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$')]),
        ),
        migrations.AddField(
            model_name='datasource',
            name='data_source_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='object_collector.DataSourceType'),
        ),
        migrations.AddField(
            model_name='datasource',
            name='data_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='object_collector.DataType'),
        ),
        migrations.AddField(
            model_name='datasource',
            name='smart_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='object_collector.SmartObject'),
        ),
        migrations.AddField(
            model_name='action',
            name='smart_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='object_collector.SmartObject'),
        ),
    ]
