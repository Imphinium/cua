from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index_mod'),
    path('logout/', views.logout_view, name='logout_mod'),
    path('input/', views.input_view, name='input_mod'),
    path('tags/', views.tags_view, name='tags_mod'),
    path('details/<str:item_id>/', views.details, name='details_mod'),
]
