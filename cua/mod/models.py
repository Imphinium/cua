from django.db import models
import secrets
import string

# Create your models here.

class IDClass():
	def newID():
		choice_set = string.ascii_uppercase + string.digits
		newID = ""
		while newID == "":
			for i in range(24):
				chosen = secrets.choice(choice_set)
				newID += chosen
		return newID

class Item(models.Model):
	id = models.CharField(primary_key=True, default=IDClass.newID, max_length=12, unique=True, editable=False)
	name = models.CharField(max_length=128)
	description = models.CharField(max_length=512)
	file = models.FileField(null=True)


	def __str__ (self):
		return f'{self.name}'