# Con archivo appsfunciones.py
from django.apps import AppConfig


class Carpeta:
	def __init__(self, nombre):
		self.nom=nombre
		self.subcarpeta=[]


	def setNom(self,direccion):
		self.nom=direccion

	
	def getNom(self):
		return self.nom

	
	def setSubcarpeta(self,nuevo ):
		self.subcarpeta.append(nuevo)


	def getSubcarpeta(self):
		return self.subcarpeta


class BlogConfig(AppConfig):
    name = 'blog'
