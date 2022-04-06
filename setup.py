import setuptools

with open('Readme.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name = 'Qsqlite',
    version = '0.95',
    author = 'Charles Lai',
    author_email = '',
    description = 'Quick Sqlite Tools',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/wolf71/Qsqlite',
    packages = ['Qsqlite'],   #setuptools.find_packages(),
    # install_requires=['matplotlib>=3.0.0'],
    entry_points={
        'console_scripts': [
            'Qsqlite = Qsqlite:main'
        ],
    },
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)