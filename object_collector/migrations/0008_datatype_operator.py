# Generated by Django 2.0.9 on 2019-01-07 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('object_collector', '0007_auto_20190107_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='datatype',
            name='operator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='object_collector.Operator'),
        ),
    ]
