from django import forms
from mod.models import Item_Request


class ItemUploadForm(forms.ModelForm):
    class Meta:
        model = Item_Request
        fields = ('name', 'description', 'file',) 