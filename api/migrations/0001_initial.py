# Generated by Django 4.1.7 on 2023-03-28 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_nombre', models.CharField(max_length=255)),
                ('s_nombre', models.CharField(max_length=255)),
                ('a_materno', models.CharField(max_length=255)),
                ('a_paterno', models.CharField(max_length=255)),
                ('rut_empleado', models.CharField(max_length=9)),
                ('email', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_empresa', models.CharField(max_length=9)),
                ('nombre_empresa', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=9)),
                ('empleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.empleados')),
            ],
        ),
        migrations.AddField(
            model_name='empleados',
            name='empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.empresas'),
        ),
    ]