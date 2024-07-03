import requests  
import mymodule
import os

def load_resource(file_path):
    file = open(file_path, 'r')
    content = file.read()
    file.close()
    return content