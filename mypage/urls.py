from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
]
# urlpatterns = [
#     path('', views.index, name='mypage.index'),
#     path('class/', views.index, name='search_box'),
# ]