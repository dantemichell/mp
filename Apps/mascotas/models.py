from django.db import models
from django.utils import timezone

# Create your models here.



class Mascota(models.Model):
	nombre = models.CharField(max_length=25)
	fecNac = models.DateField()
	imagen1 = models.ImageField(null=True, upload_to='albums/images/')
	sexoChoices = (('H','Hembra'),('M','Macho'))
	tamañoChoices =(('p','Pequeño'),('m','Mediano'),('g','Grande'))
	sexo = models.CharField(max_length=25,choices= sexoChoices)
	tamaño = models.CharField(max_length=25,choices= tamañoChoices)
	
	def __str__(self):
		return self.nombre
