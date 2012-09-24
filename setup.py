from distutils.core import setup
from setuptools import find_packages
import os.path


setup(name='tt_glossary',
      version='0.1.0',
      description='Django app for glossing and editing terms',
      author='Texas Tribune',
      author_email='tech@texastribune.org',
      url='http://github.com/texastribune/tt_glossary/',
      license='LICENSE',
      install_requires=[],
      packages=find_packages(exclude=['example_project']),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Other/NonlistedTopic'
          ],
      )
