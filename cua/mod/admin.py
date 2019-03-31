from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(Item_Request)
admin.site.register(Tag_Request)