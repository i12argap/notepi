import dropbox
import os
import sys
import webbrowser

class DropNote(object):

	def __init__(self, token):
		self.client = None
		self.app_key = 'iok20w90lywwjng'
		self.app_secret = '1ip2creb4oxs83t'
		self.app_type = 'app_folder'
		self.flow = dropbox.client.DropboxOAuth2FlowNoRedirect(self.app_key, self.app_secret)

		self.authorize_url = self.flow.start()

		if (token!=""):
			{
				self.conectar(token)
			}

	def devolverURL(self):
		return self.authorize_url.replace("api","")

	def connect(self, code):

		access_token, user_id = self.flow.finish(str(code))
		return access_token
		

#-----

	def conectar(self, token):
		
		self.client = dropbox.client.DropboxClient(token)
#-----
	

	def get_account_info(self):

	
	#Devuelve la informacion de la cuenta, como el nombre de visualizacion del usuario, la cuota, la direccion de correo electronico, etc. 
	
		return self.client.account_info()

#-----

	def list_folder(self, folder=None):

	#Devolver la informacion sobre carpetas

		lis=[]
		metadata = self.client.metadata("/")
	
		for x in metadata['contents']:

			print (x['path'].encode('utf-8'))

			if x['is_dir']==True:

				lis.append(x['path'])
		return lis

#----
#Creacion de carpetas
	def crearcarpeta(self,carpeta):
		
		self.client.file_create_folder('/'+carpeta)



#----
#Creacion de notas
	def crearnota(self, nombre, ruta):

		resultado = self.client.put_file(ruta+"/"+nombre, "",1)


#----
#Borrar carpetas
	def borrarcarpeta(self, dir):
		
		resultado = self.client.file_delete(dir)
	
#----
#Listar todas las notas 
	def listarnotas(self, folder):
		lis=[]
		metadata = self.client.metadata("/"+folder)
	
		for x in metadata['contents']:

			print(x['path'].encode('utf-8'))

			lis.append(x['path'])
		return lis

	
#----
#Borrar notas
	def borrarnota(self, ruta, folder):
		folder= ruta+"/"+folder

		resultado = self.client.file_delete(folder)


#----
#Lectura de las notas
	def leernota(self, ruta, fichero):
    
			fichero=ruta+"/"+fichero
            
			x = self.client.get_file(fichero)
            
			y=x.read()
            
			x.close()
            
			return y


#----
#Edicion de las notas
	def modificarnota(self, cambio, ruta):
		
		try:
			resultado = self.client.put_file(ruta, cambio,1)
		except:
			print("Error al guardar la nota")

