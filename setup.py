from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name="resume-matcher",
    version="0.0.2",
    author="Jyoti Kapoor",
    author_email="jyotikpr999@gmail.com",
    packages=find_packages(),
    install_reqires = get_requirements('requirements.txt')
)