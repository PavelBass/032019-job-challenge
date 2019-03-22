import os

from setuptools import (
    find_packages,
    setup,
)

setup(
    name='sibur_markov',
    version='0.0.1',
    author='Pavel Bass',
    author_email='statgg@gmail.com',
    description='Sibur job challenge',
    entry_points={
        'console_scripts': [
            'sibur_markov=sibur_markov.cli:cli',
        ],
    },
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'click==7.0',
    ],
    extras_require={
        'test': [
            'pycodestyle',
            'pylint',
            'pylint-quotes',
            'pytest',
            'pytest-cov',
            'pytest-mock',
            'diff-cover',
        ],
    },
)
