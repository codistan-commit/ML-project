from setuptools import find_packages,setup
from typing import List

hyphen_e_dot = '-e.'
def get_requirements(file_path:str)->List[str]:

    requirement = []
    with open(file_path) as file_obj:
        requirement= file_obj.readlines()
        requirement =  [req.replace("/n", "")for req in requirement]
    
        if hyphen_e_dot in requirement:
            requirement.remove(hyphen_e_dot)
    return requirement
setup(
name = 'ML project',
version = '0.0.1',
author = "Ayan",
author_email = "mohdayanmohd037@gmail.com",
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)






