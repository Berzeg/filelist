from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='filelist',

    version='1.1.2',

    description='Easily list some files in a directory, and exclude others.',
    long_description=long_description,

    url='https://github.com/Berzeg/filelist',

    author="Hashem Berzeg",
    author_email="h9.11.2s@gmail.com",

    license="MIT",

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
    ],

    keywords='directory file walk crawl .gitignore .pyignore ignore',
)