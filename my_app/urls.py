from django.urls import path
from . import views
from my_app import views
urlpatterns=[
    path('', views.home, name='home'),
    path('new_search', views.new_search, name='new_search'),


             ]