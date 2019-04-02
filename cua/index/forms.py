from django import forms
from mod.models import Item_Request


class ItemUploadForm(forms.Form):
	name = forms.CharField(max_length=128)
	description = forms.CharField(max_length=512)
	file = forms.FileField(required=False)
	repo = forms.CharField(max_length=512, required=False)
	video = forms.CharField(max_length=11, required=False)
	description = forms.CharField(max_length=512)
	tags = forms.CharField(max_length=512)
