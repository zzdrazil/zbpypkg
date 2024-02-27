from setuptools import setup

setup(
   name='zbpypkg',
   version='1.0.0',
   description='A simple Python test package',
   author='Zbynek Zdrazil',
   author_email='zbynek.zdrazil@merck.com',
   packages=['zbpypkg'],  #same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
)
