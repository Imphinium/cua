from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index_mod'),
    path('logout/', views.logout_view, name='logout_mod'),
    path('input/', views.input_view, name='input_mod'),
    path('tags/', views.tags_view, name='tags_mod'),
    path('details/<str:item_id>/', views.details, name='details_mod'),
    path('download/<str:item_id>', views.download, name='download_mod'),
    path('download/<str:item_id>/<int:read>', views.download, name='download_mod'),
    path('approve/<str:item_id>', views.approve, name='approve'),
    path('deny/<str:item_id>', views.deny, name='deny'),
]
