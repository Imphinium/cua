from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index_mod'),
    path('logout/', views.logout_view, name='logout_mod'),
]
