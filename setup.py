from distutils.core import setup
import os

# Stolen from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('glossary'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[len('glossary/'):]
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

import glossary

setup(name='glossary',
      version=glossary.__version__,
      description='Django app for glossing and editing terms',
      author='Texas Tribune',
      author_email='tech@texastribune.org',
      url='http://github.com/texastribune/tt_glossary/',
      license='LICENSE',
      install_requires=[],
      packages=packages,
      package_data={'glossary': data_files},
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
