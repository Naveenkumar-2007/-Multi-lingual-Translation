from setuptools import setup, find_packages
from typing import List

Hyper_meter=". e"
def get_requirements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath) as file:
        requirements=file.readlines()
        requirements=[re.replace("\n"," ") for re in requirements]
        if Hyper_meter in requirements:
            requirements.remove(Hyper_meter)
    return requirements



setup(
    name="multilingual-translator",
    version="0.1.0",
    author="Naveen",
    author_email="naveenkumarchapala123@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
)
