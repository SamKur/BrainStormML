from setuptools import find_packages,setup

# Read the contents of requirements.txt
with open('requirements.txt') as f:
    required_list = f.read().splitlines()
    if "-e ." in  required_list:
        required_list.remove("-e .")

setup(
    name='BrainStormML',
    version='0.1',
    author='Susamay',
    author_email='susamay.sk@gmail.com',
    packages=find_packages(), #fetches src folder, then builds py files inside of that
    # ,install_requires = get_requirements()
    install_requires=required_list,  
)