# Generated by Django 4.0.6 on 2023-03-28 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_empleados_a_materno_alter_empleados_a_paterno_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleados',
            options={'managed': True, 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.RemoveField(
            model_name='empresas',
            name='empleado',
        ),
    ]
