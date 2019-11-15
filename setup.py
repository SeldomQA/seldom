# coding=utf-8
import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('pyse/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='pyse',
    version=version,
    url='https://github.com/defnngj/pyse/',
    license='BSD',
    author='bugmaster',
    author_email='fnngj@126.com',
    description='WebUI automation testing framework based on Selenium and unittest ',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['selenium>=3.12.0', 'parameterized==0.7.0'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: Ubuntu',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries ::Testing'
    ],
    entry_points='''
        [console_scripts]
        pyse=pyse.cli:main
    '''
)
