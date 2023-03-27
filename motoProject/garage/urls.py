from django.urls import include, path

from . import views

# This file defines the URLs for the garage app. It uses the path function from 
# django.urls to map URLs to views. Each URL is associated with a specific 
# view function from views.py, which handles the HTTP requests and responses.

app_name = 'garage'
urlpatterns = [
    # ex: /garage/
    path('', views.index,name='index'),
    # ex: /garage/create/
    path('create/', views.create, name='create'),
    # ex: /garage/5/
    path('<int:motorcycle_id>/', views.description, name='description'),
    # ex: /garage/5/delete/
    path('<int:motorcycle_id>/delete/', views.delete, name='delete'),
    # ex: /garage/5/update/
    path('<int:motorcycle_id>/update/', views.update, name='update'),
]