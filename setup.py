from distutils.core import setup

version = '0.9.1'

setup(
    name='treetojson',
    version=version,
    description='Converts a tree structure into a valid JSON',
    long_description=open('README.rst').read(),
    author='Saad Sahibjan',
    author_email='saad.sahibjan@gmail.com',
    license='MIT',
    url='https://github.com/saadsahibjan/treetojson',
    py_modules=['treetojson'],
    platforms='Cross-platform',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
    ],
    install_requires=['nltk'],
)
