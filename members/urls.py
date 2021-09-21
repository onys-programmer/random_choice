from django.urls import path
from . import views

appname = 'members'
urlpatterns = [
    path('', views.index, name='index'),
]
