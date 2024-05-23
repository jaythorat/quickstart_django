import sys
import os
from utils import install_requirements,create_project,create_app,create_directories
from resources.content import index_content,css_content,app_urls_content,app_views_content,project_settings_content
# Path: main.py
def create_files(app_name : str = "sampleApp",project_name : str = "sampleProject") -> None:
    path_forHTML = f'{os.getcwd()}/templates'
    path_forCSS = f'{os.getcwd()}/static'
    html_file = 'index.html'
    css_file = 'style.css'

    # For HTML file in templates
    with open(os.path.join(path_forHTML, html_file), 'w') as fp:
        content = index_content()
        fp.write(content)

    # For CSS file in static
    with open(os.path.join(path_forCSS, css_file), 'w') as fp:
        content = css_content()
        fp.write(content)
    
    print(f"Files created ('index.html', 'style.css')")

    # For URLS.PY file in project/aplication
    path_forURLsPY = f'{os.getcwd()}/{app_name}'
    with open(os.path.join(path_forURLsPY, 'urls.py'), 'w') as fp:
        content = app_urls_content(app_name)
        fp.write(content)
    print(f"URLS.PY file created in {app_name}")
    
    # For VIEWS.PY file in project/aplication
    path_forViewsPY = f'{os.getcwd()}/{app_name}'   
    with open(os.path.join(path_forViewsPY, 'views.py'), 'w') as fp:
        content = app_views_content()
        fp.write(content)
    print(f"VIEWS.PY file created in {app_name}")
    
    
    # For settings.py file in project
    path_forSettingsPY = f'{os.getcwd()}/{project_name}' 
    with open(os.path.join(path_forSettingsPY, "settings.py"), 'a') as fp:
        content = project_settings_content()
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
    base_path = os.getcwd()
    required_package = 'django'
    install_requirements(required_package)
    
    create_project()
    create_app()
    create_directories(["templates","static","media"])
    create_files()
    
if __name__ == '__main__':
    quickstart_django()
