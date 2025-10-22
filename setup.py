from setuptools import find_packages, setup

setup(
    name="medi_bot",
    version="0.1.0",
    author="Pavan Jakkampudi",
    author_email="jps09871@gmail.com",
    packages=find_packages(), #it will try to find counstructor file. So whereever it will see the constructor file that folder will be insalled as a local package
    install_requires=[]  #it will automatically try to sence requiremnts file in project and install all the dependencies mentioned in requirements file
)

#Here setup file is helping to install any kinds of folders as a local package because here we'll following modular coding, we will import some functions from different modules for that we need setup file to install those modules as local packages  