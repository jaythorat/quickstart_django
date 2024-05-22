import sys
import os

base_path = os.getcwd()
# print(base_path)
# project_name = sys.argv[1]
# app_name = sys.argv[2]

def install_requirements(module_name : str) -> None:
    try:
        os.system(f"pip install {module_name}")
    except:
        print(f"Failed: Unable to install module {module_name}")

def create_directory(dir_name : str) -> None:
    try:
        os.system(f"mkdir {dir_name}")
    except:
        print(f"Failed : Unable to create directory {dir_name}")

def create_directories(essential_dirs : list[str]) -> None:
    for dir in essential_dirs:
        create_directory(f"{dir}")

def create_project(project_name : str = "sampleProject") -> None:
    os.system(f'django-admin startproject {project_name}')
    os.chdir(f'{project_name}')
    print(f"Project {project_name} initialized")

def create_app(app_name : str = "sampleApp") -> None:
    os.system(f'django-admin startapp {app_name}')
    print(f"Application {app_name} created")

# Path: main.py
def create_files(app_name : str = "sampleApp",project_name : str = "sampleProject"):
    path_forHTML = f'{os.getcwd()}/templates'
    path_forCSS = f'{os.getcwd()}/static'
    html_file = 'index.html'
    css_file = 'style.css'

    # For HTML file in templates
    with open(os.path.join(path_forHTML, html_file), 'w') as fp:
        content = """
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

</html>"""
        fp.write(content)

    # For CSS file in static
    with open(os.path.join(path_forCSS, css_file), 'w') as fp:
        content = """body{
        background-color: #f1f1f1;
    }
        """
        fp.write(content)
    
    print(f"Files created ('index.html', 'style.css')")

    # For URLS.PY file in project/aplication
    path_forURLsPY = f'{os.getcwd()}/{app_name}'
    with open(os.path.join(path_forURLsPY, 'urls.py'), 'w') as fp:
        content = f"""from django import views
from django.urls import path
from {app_name} import views
import os
urlpatterns = [
    path('', views.index, name='index'),
]
"""
        fp.write(content)
    print(f"URLS.PY file created in {app_name}")
    # For VIEWS.PY file in project/aplication
    path_forViewsPY = f'{os.getcwd()}/{app_name}'   
    with open(os.path.join(path_forViewsPY, 'views.py'), 'w') as fp:
        content = f"""from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
"""
        fp.write(content)
    
    print(f"VIEWS.PY file created in {app_name}")
    # For settings.py file in project
    path_forSettingsPY = f'{os.getcwd()}/{project_name}' 
    with open(os.path.join(path_forSettingsPY, "settings.py"), 'a') as fp:
        content = f"""#Added via Django Starter Module for static files
STATICFILES_DIRS = [
     BASE_DIR / "static"
]
"""
        fp.write(content)
    print(f"STATICFILES_DIRS added in settings.py")

    with open(os.path.join(path_forSettingsPY, "settings.py"), 'r+') as fp:
        content = fp.read()
        list = content.split("\n")
        for i in list:
            if "INSTALLED_APPS" in i:
                list.insert(list.index(i)+1, f"    '{app_name}.apps.{app_name.capitalize()}Config',")
            
            if "TEMPLATES = [" in i:
                template_dir = list.index(i)+3
                list[template_dir]=f"        'DIRS': [BASE_DIR / 'templates'],"

        result = ""
        for i in range(len(list)):
            result += list[i]
            result += "\n"
        fp.seek(0)
        fp.write(result)
    print(f"INSTALLED_APPS added in settings.py")
    # For urls.py file in project
    path_forURLsPY_project = f'{os.getcwd()}/{project_name}'
    with open(os.path.join(path_forURLsPY_project, "urls.py"), 'r+') as fp:
        content = fp.read()
        list = content.split("\n")
        for i in list:
            if "from django.contrib import admin" in i:
                list.insert(list.index(i)+1, f"from django.urls import include")
            if "urlpatterns = [" in i:
                list.insert(list.index(i)+1, f"    path('', include('{app_name}.urls')),")

        print(len(list))
        result = ""
        for i in range(len(list)):
            result += list[i]
            result += "\n"
        fp.seek(0)
        fp.write(result)
    print(f"URLS.PY file updated in {project_name}")
    print(f"""
{"*"*100}
Django Starter Package is ready to use
cd into {project_name} 
          & 
run python manage.py runserver
{"*"*100}
    """)

def quickstart_django():
    create_project()
    create_app()
    create_directories(["templates","static","media"])
    create_files()
    
if __name__ == '__main__':
    quickstart_django()
