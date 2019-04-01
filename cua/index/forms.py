from django import forms
from mod.models import Item_Request


class ItemUploadForm(forms.Form):
	name = forms.CharField(max_length=128)
	description = forms.CharField(max_length=512)
	file = forms.FileField()
	tags = forms.CharField(max_length=512)
