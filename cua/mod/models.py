from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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

class Tag(models.Model):
	name = models.CharField(primary_key=True, max_length=128, editable=True)
	creation_date = models.DateTimeField(default=timezone.now)
	creator = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return f'{self.name}'

class Item(models.Model):
	id = models.CharField(primary_key=True, default=IDClass.newID, max_length=12, editable=False)
	name = models.CharField(max_length=128)
	former_name = models.CharField(max_length=128, null=True, blank=True, default=None)
	description = models.CharField(max_length=512)
	former_description = models.CharField(max_length=512, null=True, blank=True, default=None)
	file = models.FileField(upload_to="files/{0}".format(IDClass.newID()))
	creation_date = models.DateTimeField(default=timezone.now)
	creator = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.SET_DEFAULT)
	tags = models.ManyToManyField(Tag)


	def __str__ (self):
		return f'{self.name}'

class Item_Request(models.Model):
	id = models.CharField(primary_key=True, default=IDClass.newID, max_length=12, editable=False)
	name = models.CharField(max_length=128)
	description = models.CharField(max_length=512)
	file = models.FileField(upload_to="files/{0}".format(IDClass.newID()))
	creation_date = models.DateTimeField(default=timezone.now)
	creator = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.SET_DEFAULT)
	tags = models.ManyToManyField(Tag)


	def __str__ (self):
		return f'{self.name}'
