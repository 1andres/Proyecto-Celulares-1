#from rest_framework import serializers
from Celulares.apps.ventas.models import Celular, Marca, Color, Conectividad

class celular_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Celular
		fields = ('url','color','conectividad', 'modelo','sistema_opearativo','tamanio_pantalla','peso','bateria','memoria','radio','accesorios','imagen','status')

class marca_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Marca
		fields = ('url','marca')

class color_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Color
		fields = ('url','color')

class conectividad_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Conectividad
		fields = ('url','conectividad')