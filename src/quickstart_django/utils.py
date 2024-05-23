import os

def install_requirements(module_name : str) -> None:
    try:
        os.system(f"pip install {module_name}")
    except:
        print(f"Failed: Unable to install module {module_name}")
        
def create_project(project_name : str = "sampleProject") -> None:
    os.system(f'django-admin startproject {project_name}')
    os.chdir(f'{project_name}')
    print(f"Project {project_name} initialized")
    
def create_app(app_name : str = "sampleApp") -> None:
    os.system(f'django-admin startapp {app_name}')
    print(f"Application {app_name} created")
    
def create_directory(dir_name : str) -> None:
    try:
        os.system(f"mkdir {dir_name}")
    except:
        print(f"Failed : Unable to create directory {dir_name}")

def create_directories(essential_dirs : list[str]) -> None:
    for dir in essential_dirs:
        create_directory(f"{dir}")