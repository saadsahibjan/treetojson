from distutils.core import setup

version = '0.1'

setup(
    name='treetojson',
    version=version,
    description='Converts a tree structure in to a valid JSON',
    long_description=open('README.md').read(),
    author='Saad Sahibjan',
    author_email='saad.sahibjan@gmail.com',
    license='LICENSE',
    url='https://github.com/saadsahibjan/treetojson',
    py_modules=['treetojson'],
    platforms='Cross-platform',
)
