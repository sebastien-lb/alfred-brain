from django.db import migrations

def add_datatypes_operators(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    DataType = apps.get_model("object_collector", "DataType")
    datatypes_keys = ['color']
    datatypes = {k: DataType.objects.using(db_alias).filter(name=k) for k in datatypes_keys}
    for k in datatypes:
        if datatypes[k].count() == 0:
            DataType(name=k).save()


class Migration(migrations.Migration):

    dependencies = [
        ('object_collector', '0020_auto_20190213_1247'),
    ]

    operations = [migrations.RunPython(add_datatypes_operators)]
