from django import forms
from mod.models import Item


class ItemUploadForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'file',) 