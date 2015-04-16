# Create your views here.
from django.http import HttpResponse
from Celulares.apps.ventas.models import *
from django.core import serializers
from .serializer import *
from rest_framework import viewsets


def ws_productos_view(request):
	data = serializers.serialize("json", Celular.objects.filter(status = True))
	return HttpResponse(data, mimetype='application/json')

class celular_viewset(viewsets.ModelViewSet):
	queryset = Celular.objects.all()
	serializer_class = celular_serializer

class marca_viewset(viewsets.ModelViewSet):
	queryset = Marca.objects.all()
	serializer_class = marca_serializer

class color_viewset(viewsets.ModelViewSet):
	queryset = Color.objects.all()
	serializer_class = color_serializer

class conectividad_viewset(viewsets.ModelViewSet):
	queryset = Conectividad.objects.all()
	serializer_class = conectividad_serializer