import dropbox
import os
import sys
import webbrowser
from dropbox import DropboxOAuth2FlowNoRedirect
class DropNote(object):

	def __init__(self, token):
		self.client = None
		self.app_key = 'iok20w90lywwjng'
		self.app_secret = '1ip2creb4oxs83t'
		self.app_type = 'app_folder'
		self.flow = DropboxOAuth2FlowNoRedirect(self.app_key, self.app_secret)

		self.authorize_url = self.flow.start()

		if (token!=""):
			{
				self.conectar(token)
			}

	def devolverURL(self):
		return self.authorize_url.replace("api","")

	def connect(self, code):
    
		resultado = self.flow.finish(str(code))
		return resultado.access_token

		

#-----

	def conectar(self, token):
		
		self.client = dropbox.Dropbox(token)
#-----
	

	def get_account_info(self):

	
	#Devuelve la informacion de la cuenta, como el nombre de visualizacion del usuario, la cuota, la direccion de correo electronico, etc. 
	
		return self.client.account_info()

#-----

	def list_folder(self, folder=None):

	#Devolver la informacion sobre carpetas

		lis=[]
		metadata = self.client.files_list_folder("")
	
		for x in metadata.entries:

			print (x.path_lower.encode('utf-8'))

			if self.client.files_list_folder(x.path_lower):

				lis.append(x.path_lower)
		return lis

#----
#Creacion de carpetas
	def crearcarpeta(self,carpeta):
		
		self.client.files_create_folder('/'+carpeta)



#----
#Creacion de notas
	def crearnota(self, nombre, ruta):

		resultado = self.client.resultado = self.client.files_upload(str.encode(""),"/"+ruta+"/"+nombre)


#----
#Borrar carpetas
	def borrarcarpeta(self, dir):
		
		resultado = self.client.files_delete("/"+dir)
	
#----
#Listar todas las notas 
	def listarnotas(self, folder):
		lis=[]
		metadata = self.client.files_list_folder("/"+folder)
	
		for x in metadata.entries:

			print(x.path_lower.encode('utf-8'))

			lis.append(x.path_lower)
		return lis
	
#----
#Borrar notas
	def borrarnota(self, ruta, folder):
		folder= "/"+ruta+"/"+folder

		resultado = self.client.files_delete(folder)

#----
#Lectura de las notas
	def leernota(self, ruta, fichero):
    
		fichero="/"+ruta+"/"+fichero
            
		x,res = self.client.files_download(fichero)
            
		return res.content

#----
#Edicion de las notas
	def modificarnota(self, cambio, ruta):

		resultado = self.client.files_upload(cambio,ruta,mode=dropbox.files.WriteMode('overwrite', None))


