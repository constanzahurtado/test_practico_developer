from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('database/', views.data, name = 'database'),

]
