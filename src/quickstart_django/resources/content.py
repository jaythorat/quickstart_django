def index_content() -> str:
    return """ 
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Djaango Starter Package</title>
    {% load static%}
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>

<body>
    <h2>Welcome to Django Starter!!!</h2>
</body>

</html>
"""

def css_content() -> str:
    return """ 
body{
        background-color: #f1f1f1;
    }
"""

def app_urls_content(app_name : str) -> str:
    return """
from django import views
from django.urls import path
from {app_name} import views
import os
urlpatterns = [
    path('', views.index, name='index'),
]
"""

def app_views_content() -> str:
    return """ 
from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    
"""

def project_settings_content() -> str:
    return """#Added via Django Starter Module for static files
STATICFILES_DIRS = [
     BASE_DIR / "static"
]
"""