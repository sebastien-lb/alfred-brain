# Generated by Django 2.0.9 on 2019-01-15 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('object_collector', '0009_auto_20190107_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionScenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payload', models.BinaryField()),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='object_collector.Action')),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='object_collector.Scenario')),
            ],
            options={
                'verbose_name_plural': 'ActionScenarios',
            },
        ),
    ]