# Generated by Django 4.0.6 on 2023-03-28 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_empleados_options_alter_empresas_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='a_materno',
            field=models.CharField(max_length=255, verbose_name='Apellido Materno'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='a_paterno',
            field=models.CharField(max_length=255, verbose_name='Apellido Paterno'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='email',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='p_nombre',
            field=models.CharField(max_length=255, verbose_name='Primer Nombre'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='s_nombre',
            field=models.CharField(max_length=255, verbose_name='Segundo Nombre'),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.empleados', verbose_name='Empleado'),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='nombre_empresa',
            field=models.CharField(max_length=255, verbose_name='Nombre Empresa'),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='rut_empresa',
            field=models.CharField(max_length=9, verbose_name='Rut Empresa'),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='telefono',
            field=models.CharField(max_length=9, verbose_name='Teléfono'),
        ),
    ]