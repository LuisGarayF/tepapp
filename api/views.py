from django.shortcuts import render
from api.models import Empresas, Empleados
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Empresas

class EmpresaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            empresas= list(Empresas.objects.filter(id=id).values())

            if len(empresas) > 0:
                empresa = empresas[0]
                datos = {'message':'Success','empresa':empresa}
            else:
                datos = {'message':'No hay empresas agregadas'}

            return JsonResponse(datos)

        else:
            empresas= list(Empresas.objects.values())

            if len(empresas) > 0:
                datos = {'message':'Success','empresas':empresas}
            else: 
                datos = {'message':'No hay empresas agregadas'}

            return JsonResponse(datos)

    def post(self, request):

        jd = json.loads(request.body)
        Empresas.objects.create(rut_empresa=jd['rut_empresa'],nombre_empresa=jd['nombre_empresa'],telefono=jd['telefono'])
        datos = {'message':'Success'}

        return JsonResponse(datos)

    def put(self, request, id):

        jd = json.loads(request.body)
        empresas= list(Empresas.objects.filter(id=id).values())

        if len(empresas) > 0:

            empresa= Empresas.objects.get(id=id)
            nombre_empresa= jd['nombre_empresa']
            rut_empresa= jd['rut_empresa']
            telefono= jd['telefono']
            empresa.save()
            datos = {'message':'Success'}

        else:
            datos = {'message':'No hay empresas agregadas'} 

        return JsonResponse(datos) 

    def delete(self, request,id):
        empresas= list(Empresas.objects.filter(id=id).values())

        if len(empresas) > 0:

            Empresas.objects.filter(id=id).delete()
            datos = {'message':'Success'}

        else:  
             datos = {'message':'No hay empresas agregadas'}

        return JsonResponse(datos)  