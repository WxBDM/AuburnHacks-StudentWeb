"""studentweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from overview.views import overview_page
from assignment_manager.views import assignmentHTML
from dashboard.views import home_page
from grade_manager.views import gradesHTML
from settings.views import settingsHTML
from notes_manager.views import notesHTML

urlpatterns = [
    path('admin/', admin.site.urls),
    path('settings.html', settingsHTML),
    path('grades_manager.html', gradesHTML),
    path('dashboard.html', home_page),
    path('assignment_manager.html', assignmentHTML),
    path('class_overview.html', overview_page),
    path('notes_manager.html', notesHTML)
]
