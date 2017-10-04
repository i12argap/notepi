from django.forms import ModelForm
from note.models import Persona
from django import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from ideia_summernote.fields import *

class forma(ModelForm):
	class Meta:
		model = Persona
		fields = { 
			'nombre',
			'token',
			'edad',
		} 
 

class SingUpForm(ModelForm):
        password = forms.CharField(widget=forms.PasswordInput(render_value = False), required = True) 
class Meta:
		model = User
		fields = ['username', 'password', 'first_name', 'email']	
		widgets = {
			'password': forms.PasswordInput(),		
		}

class LoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput())

class NuevaCarpeta(forms.Form):
	nombrecarpeta = forms.CharField(max_length=100)

class NuevaNota(forms.Form):
	nota = forms.CharField(max_length=100)

class BookForm(forms.Form):
		text =forms.CharField(widget=SummernoteWidget())
