from setuptools import setup, find_packages
from typing import List


# Declaring variables for setup function
PROJECT_NAME= "housing-predictor"
VERSION="0.0.1"
AUTHOR="Md Sanowar Hossain"
DESCRIPTION="Housing price prediction"
#PACKAGES=['housing']
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:

    """
    Description: This function is going to return list of requirements.
    mention in requirements.txt requirement_file.

    return This function is going to retun a list which contain name.
    of libraries mentioned in requirements.txt file.
    example return : ['pandas', 'numpy']

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()

)

# check this function is working or not

