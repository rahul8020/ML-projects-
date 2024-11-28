from setuptools import find_packages,setup
from typing import List 

def get_requirments(file_path:str)->List[str]:
    '''
    this function will return the list of requirments 
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[ req.replace("/n","") for req in requirments]  ## because it txt file has the /n as new line
setup(
    name = 'mlproject',
    version='0.0.1',
    author='J Rahul',
    author_email='rahuljagtap326@gmail.com',
    packages=find_packages(),
    install_requires = get_requirments('requirments.txt')
)