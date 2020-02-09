from django.urls import path
from . import views

# Create your urls here - SETTINGS

urlpatterns = [
    path('', views.notesHTML, name = 'settings')        
]
