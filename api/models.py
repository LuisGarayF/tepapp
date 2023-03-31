from django.db import models
from django.contrib.auth.models import User

class Empresas(models.Model):
    rut_empresa = models.CharField(max_length=9,null= False, blank=False, verbose_name="Rut Empresa")
    nombre_empresa = models.CharField(max_length=255,null= False, blank=False, verbose_name="Nombre Empresa")
    telefono = models.CharField(max_length=9,null= False, blank=False, verbose_name="Teléfono")
    #empleado = models.ForeignKey('Empleados', on_delete=models.CASCADE,null=True, verbose_name="Empleado")

    class Meta:
            managed = True
            db_table = 'Empresas'
            verbose_name = "Empresa"
            verbose_name_plural = 'Empresas'

    def __str__(self):
         return f'{self.rut_empresa}{self.nombre_empresa}{self.telefono}'

class Empleados(models.Model):
    rut_empleado = models.CharField(max_length=9,null= False, blank=False)
    p_nombre = models.CharField(max_length=255, verbose_name="Primer Nombre",null= False, blank=False)
    s_nombre = models.CharField(max_length=255,  verbose_name="Segundo Nombre",null= False, blank=False)
    a_paterno = models.CharField(max_length=255,  verbose_name="Apellido Paterno",null= False, blank=False)
    a_materno = models.CharField(max_length=255,  verbose_name="Apellido Materno",null= False, blank=False)
    empresa = models.ForeignKey('Empresas', on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=300,null= True, blank=True)

    class Meta:
            managed = True
            db_table = 'Empleados'
            verbose_name = "Empleado"
            verbose_name_plural = 'Empleados'

    def __str__(self):
         return f'{self.p_nombre}{self.s_nombre}{self.a_paterno}{self.a_materno}{self.empresa}{self.rut_empleado}{self.email}'