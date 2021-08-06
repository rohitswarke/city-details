"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject

To build run the command: python setup.py bdist_wheel
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib
from glob import glob

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

name, __version__ = "", ""
exec(compile(open('./city_details/__version__.py').read(),
             './city_details/__version__.py', 'exec'))

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().splitlines()

print("%s - Building version %s" % (name, __version__))

setup(
    name=name,
    version=__version__,
    description='city-details web portal',  # Optional

    long_description=long_description,  # Optional

    long_description_content_type='text/markdown',  # Optional (see note above)

    url='https://github.com/rohitswarke/city-details',  # Optional

    author='Rohit Warke',  # Optional

    author_email='rohitswarke@gmail.com',  # Optional

    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],

    include_package_data=True,

    keywords='mongodb, fastapi',  # Optional

    packages=find_packages(
        include=['city_details', 'city_details.*']
    ),  # Required

    data_files=[
        ('custom_logger', glob('city_details/core/*.json'))
    ],

    python_requires='>=3.6, <4',

    install_requires=requirements,  # Optional

    extras_require={  # Optional
        'dev': ['pytest'],
        'test': ['coverage', 'pytest'],
    }
)