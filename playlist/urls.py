from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='playlist_index'),
    path('<int:playlist_id>/', views.index, name='playlist_id'),
    path('<int:playlist_id>/edit', views.index, name='playlist_edit'),
    path('register', views.index, name='playlist_register'),
]