from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Persona(models.Model):
	user = models.CharField(max_length=100)
	token = models.CharField(max_length=50)
	nombre = models.CharField(max_length=100, null=True)
	edad = models.IntegerField(null=True)

	def __str__(self):
		return self.nombre
