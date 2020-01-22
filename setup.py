"""A setuptools based setup module."""
from os import path
from io import open
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ghost_blog_automation',
    version='0.0.1',
    description='Sanitize content & automatically backup your Ghost Blog.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/toddbirchard/ghost-blog-automation',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='Ghost blog SQL automation API admin SEO tool',
    packages=find_packages(),
    install_requires=['Pyjwt',
                      'Requests',
                      'Loguru',
                      'Python-dotenv'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'run=wsgi:init',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/toddbirchard/ghost-blog-automation/issues',
        'Source': 'https://github.com/toddbirchard/ghost-blog-automation/',
    },
)
