from django.db import models

# Create your models here.

class Marca(models.Model):
	marca      = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.marca

class Color(models.Model):
	color      = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.color

class Conectividad(models.Model):
	conectividad         = models.CharField(max_length = 500)
	def __unicode__(self):
		return self.conectividad
		

class Celular(models.Model):

	def url(self, filename):
		ruta = "MultimediaData/celular/%s/%s"%(self.modelo, str(filename))
		return ruta
	marca			    = models.ForeignKey(Marca)
	color               = models.ForeignKey(Color)
	conectividad        = models.ManyToManyField(Conectividad)
	modelo              = models.CharField(max_length = 500)
	sistema_opearativo  = models.CharField(max_length = 500)
	tamanio_pantalla    = models.CharField(max_length = 500)
	peso			    = models.CharField(max_length = 500)
	bandas			    = models.CharField(max_length = 500)
	bateria 			= models.CharField(max_length = 500)
	memoria 			= models.CharField(max_length = 500)
	radio    		    = models.BooleanField(default = True)
	accesorios 			= models.BooleanField(default = True)
	imagen		    	= models.ImageField(upload_to= url, null = True, blank = True)
	status			    = models.BooleanField(default = True)


	def __unicode__(self):
		return self.marca.marca+" "+ self.modelo+" "+self.color.color
	
		