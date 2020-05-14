import os
import shutil


def create_directories(*directories):
    
    for directory in directories:
        if (not os.path.exists(directory)):
            print(
                "Creating directory: {directory}".format(
                    directory = directory))
            try:  
                os.makedirs(directory)
            except OSError:  
                print(
                    "Cannot create directory: {directory}".format(
                        directory = directory))


def delete_directories(*directories):
        
    for directory in directories:
        if (os.path.exists(directory)):
            print(
                "Deleting directory: {directory}".format(
                    directory = directory))
            shutil.rmtree(directory)