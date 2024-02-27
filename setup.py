from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
   name='zbpypkg',
   version='1.0.0',
   description='A simple Python test package',
   author='Zbynek Zdrazil',
   author_email='zbynek.zdrazil@merck.com',
   packages=['zbpypkg'],  #same as name
   keywords = "test",
   python_requires=">=3.6, <4",
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
   project_urls={  # Optional
        "Bug Reports": "https://github.com/zzdrazil/zbpypkg/issues",
        "Source": "https://github.com/zzdrazil/zbpypkg.git",
    },
)
