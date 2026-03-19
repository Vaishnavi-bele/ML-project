from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path ) as file_obj:  
        '''        This will read the requirements.txt file and return the list of requirements'''
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]  #This will remove the newline character from the requirements
        if HYPEN_E_DOT in requirements: 
            requirements.remove(HYPEN_E_DOT) 
            # This will remove the -e . from the requirements why?  because it is not a requirement that needs to be installed, it is just a way to install the current package in editable mode. So we need to remove it from the requirements list before installing the requirements.
    return requirements 

setup( 
    name='mlproject',
    version='0.1.0',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
    author='Vaishnavi Bele',
    author_email='vaishnavibele693@gmail.com',
    description='A simple machine learning project'
)