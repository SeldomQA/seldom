# coding=utf-8
import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('seldom/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open("description.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='seldom',
    version=version,
    url='https://github.com/seldomQA/seldom/',
    license='BSD',
    author='bugmaster',
    author_email='fnngj@126.com',
    description='WebUI automation testing framework based on Selenium and unittest.',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'selenium>=3.12.0',
        'parameterized==0.7.0',
        'colorama>=0.4.3',
        'openpyxl>=3.0.3'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Topic :: Software Development :: Testing",
    ],
    entry_points='''
        [console_scripts]
        seldom=seldom.cli:main
    '''
)
