import os

from setuptools import setup, find_packages

from michal_theme import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='blog-michal-theme',
    version=__version__,
    include_package_data=True,
    license='BSD License',
    packages=find_packages(),
    description='A Simple Theme.',
    long_description=README,
    url='https://michal.g10f.de',
    author='Gunnar Scherf',
    author_email='mail@g10f.de',
    install_requires=['wagtail'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Wagtail',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
