import os
from pathlib import Path
import logging

project_name = "datascience"

list_of_files = [

            f"src/{project_name}/__init__.py",
            f"src/{project_name}/components/__init__.py",
            f"src/{project_name}/utils/__init__.py",
            f"src/{project_name}/config/__init__.py",
            f"src/{project_name}/config/configuration.py",
            f"src/{project_name}/pipeline/__init__.py",
            f"src/{project_name}/entity/__init__.py",
            f"src/{project_name}/entity/config_entity.py",
            f"src/{project_name}/constant/__init__.py",
            f"src/{project_name}/utils/__init__.py",
            f"src/{project_name}/utils/common.py",
            "config/config.yaml",
            "params.yaml",
            "schema.yaml",
            "main.py",
            'Dockerfile',
            "setup.py", ## I will use it if I want to upload my code to pypy as package (not needed, can ignore this)
            "templates/index.html",
            "app.py"


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = filepath.parent,filepath.name

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
        logging.info("creating empty file")

    else:
        logging.info("File already exist")

