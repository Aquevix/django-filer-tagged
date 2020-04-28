#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from filer import __version__


REQUIREMENTS = [
    'django>=1.11,<4.0',
    'django-mptt>=0.6,<1.0',  # the exact version depends on Django
    'django_polymorphic>=0.7,<2.2',
    'easy-thumbnails>=2,<3.0',
    'Unidecode>=0.04,<1.2',
    'django-taggit>=1.1.0',
    'six',
]


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Framework :: Django',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.2',
    'Framework :: Django :: 3.0',
    'Framework :: Django CMS',
    'Framework :: Django CMS :: 3.4',
    'Framework :: Django CMS :: 3.5',
    'Framework :: Django CMS :: 3.6',
    'Framework :: Django CMS :: 3.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
]


setup(
    name='django-filer-tagged',
    version=__version__,
    author='Aquevix, Divio AG',
    author_email='info@aquevix.com',
    url='https://github.com/Aquevix/django-filer-tagged',
    license='BSD',
    description='Custom port of django-filer: A file management application for django that makes handling '
                'of files and images a breeze.',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    test_suite='tests.settings.run',
)
