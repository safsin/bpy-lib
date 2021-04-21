#!/home/mrobotics-33040/anaconda3/envs/py36/bin/python python

from setuptools import setup, find_packages

setup(name='bpy2',
      version='1.0.0',
      description='A compiled binary of Blender-as-a-Python-Module (bpy) for use in AWS Lambda',
      author='Benjamin Congdon',
      author_email='me@bcon.gdn',
      url='https://github.com/bcongdon/bpy_lambda',
      package_dir={"": "src"},
      packages=find_packages(where="src"),
      package_data={"": ["2.79", "*.so"]},
      include_package_data=True,
      python_requires=">=3.6"
      )
