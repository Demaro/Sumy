#! / Usr / bin / python env
# - * - coding: UTF-8 - * -

from django.db import models

from django.contrib.auth.models import User


from django.conf import settings



class Message(models.Model):
	user = models.ForeignKey(User,related_name="secretaria")
	emisor_nn = models.CharField(max_length=20, null=True, blank=True)
	emisor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
	receptor   = models.ForeignKey(User,related_name="receptor")
	fecha_inicio = models.DateField(null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	fecha_fin = models.DateField(null=True, blank=True)
	cod_valid = models.CharField(max_length=20)
	estado  = models.CharField(max_length=10)




class Profile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	rut  = models.CharField(max_length=20)
	birthdate = models.DateField()

	departamento = models.ForeignKey('Departamento')
	inicio_cargo = models.DateField(auto_now=True, auto_now_add=False)


	def __str__(self):
		return self.user


class Departamento(models.Model):
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre


	
