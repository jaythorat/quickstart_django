import os

def install_requirements(module_name : str) -> None:
    try:
        os.system(f"pip install {module_name}")
    except:
        print(f"Failed: Unable to install module {module_name}")