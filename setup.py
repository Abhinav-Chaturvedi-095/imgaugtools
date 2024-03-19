from setuptools import setup, find_packages
 
setup(
    name='imgaugtools',
    version='1.0.5',
    packages=find_packages(),
    install_requires=[
        # List of dependencies
        "numpy>=1.0",
        "opencv-python>=4.5.1",
        "scipy>=1.8.0",
    ],
    author='Abhinav Chaturvedi',
    description='easy to use image augmentation tool',
    Long_description=open("README.md").read()
)