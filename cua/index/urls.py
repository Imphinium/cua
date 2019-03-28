from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
import os

suburl = '';
# If the env var is not empty, and if its value isn't "default", append the suburl.
if os.environ['SUBURL'] and os.environ['SUBURL'] != 'default':
    suburl = os.environ['SUBURL']

urlpatterns = [
    path(suburl, views.index, name='index'),
    path(suburl + '/results/', views.results, name='results'),
    path(suburl + '/details/<str:item_id>/', views.details, name='details'),
    pathsuburl(suburl + '/upload/', views.upload, name='upload'),
]
