import os


def install_requirements(module_name: str) -> None:
    """
    Installs requirements for the module.
    """
    try:
        os.system(f"pip install {module_name}")
    except:
        print(f"Failed: Unable to install module {module_name}")


def create_project(project_name: str = "sampleProject") -> None:
    """
    Initializes the project using `django-admin startproject projectname` command.
    """
    print(f"Initializing project {project_name}")
    os.system(f"django-admin startproject {project_name}")
    os.chdir(f"{project_name}")
    print(f"Project {project_name} initialized")


def create_app(app_name: str = "sampleApp") -> None:
    """
    Initializes the application using `django-admin startapp appname` command.
    """
    os.system(f"django-admin startapp {app_name}")
    print(f"Application {app_name} created")


def create_directory(dir_name: str) -> None:
    try:
        os.system(f"mkdir {dir_name}")
    except:
        print(f"Failed : Unable to create directory {dir_name}")


def create_directories(essential_dirs: list[str]) -> None:
    """
    Creates essential dirs.
    """
    for dir in essential_dirs:
        create_directory(f"{dir}")
