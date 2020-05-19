import shutil
from pathlib import Path


def create_directories(*directories):
    
    for directory in directories:
        d = Path(directory)
        if (not d.exists()):
            print(
                "Creating directory: {directory}".format(
                    directory = directory))
            try:  
                d.mkdir(parents = True, exist_ok = True)
            except OSError:  
                print(
                    "Cannot create directory: {directory}".format(
                        directory = directory))


def delete_directories(*directories):
        
    for directory in directories:
        d = Path(directory)
        if (d.exists()):
            print(
                "Deleting directory: {directory}".format(
                    directory = directory))
            shutil.rmtree(d)