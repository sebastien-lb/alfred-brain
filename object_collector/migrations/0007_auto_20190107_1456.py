# Generated by Django 2.0.9 on 2019-01-07 14:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('object_collector', '0006_remove_datasource_entrypoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.BinaryField()),
                ('data_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='object_collector.DataSource')),
            ],
            options={
                'verbose_name_plural': 'Conditions',
            },
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Operators',
            },
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('action', models.ManyToManyField(to='object_collector.Action')),
            ],
            options={
                'verbose_name_plural': 'Scenarios',
            },
        ),
        migrations.AddField(
            model_name='condition',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='object_collector.Operator'),
        ),
        migrations.AddField(
            model_name='condition',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='object_collector.Scenario'),
        ),
    ]
