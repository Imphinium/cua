from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('details/<str:item_id>/', views.details, name='details'),
    path('upload/', views.upload, name='upload'),
    path('download/<str:item_id>/', views.download, name='download'),
]
