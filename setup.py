from setuptools import find_packages,setup

HYPEN_E_DOT="-e ."

def get_require(file_path):
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Narendra",
    author_email="ns172128561@gmail.com",
    packages=find_packages(),
    install_requires=get_require("requirements.txt")
)