# coding: utf-8
from setuptools import setup, find_packages
import rest

# entry_points
entry_points = {
    'console_scripts':[
        "api = rest.cli.api:cli",
    ]
}

# requires
with open('requirement.txt') as f:
    requires = [exts for exts in f.read().splitlines() if exts]


setup(
    name='rest',
    version='0.3',
    packages=find_packages(),
    include_package_data=True,
    description='simple flask restful api lib',
    long_description=open('README.md').read(),
    url='https://github.com/neo1218/rest',
    author='neo1218',
    author_email='neo1218@yeah.net',
    license='MIT',
    keywords='flask restful api',
    install_requires=requires,
    entry_points=entry_points,
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
