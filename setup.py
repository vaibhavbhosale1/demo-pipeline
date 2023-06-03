from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author="vaibhav",
      author_email="vaibhavbhosalesvb4@gmail.com",
      packages=find_packages(),
      install_requirements=["pandas","numpy","flask"]
      
      )