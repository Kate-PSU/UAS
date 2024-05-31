from django.urls import path

from . import views

app_name = 'dictionary'

urlpatterns = [
    path('', views.index, name='index'),
    path('definition/', views.definition, name='definition'),
]