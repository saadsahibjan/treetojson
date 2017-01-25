from distutils.core import setup

version = '0.0.4'

setup(
    name='treetojson',
    version=version,
    description='Converts a tree structure in to a valid JSON',
    #long_description=open('README.md').read(),
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
        'Programming Language :: Python :: 3',
    ],
    install_requires=['nltk'],
)
