import re
from os import path
from setuptools import setup, find_packages

# --------------------------------------------------------------------------------------------
pkg_name = 'netvision'
git_url = 'https://github.com/palanglois/netvision'
description = 'Fuel your collaborations by sending awesome webpage results. Forget about HTML and CSS and Javascript, just effortlessly use Python.'
author = 'Pierre-Alain Langlois, Thibault Groueix'
author_email = ''
# --------------------------------------------------------------------------------------------


def get_version(*package_path):
    '''
    Return package version as listed in __version__ in init.py.
    '''
    print(*package_path)
    with open(path.join(*package_path, '__init__.py')) as f:
        for line in f.readlines():
            res = re.search(r"^__version__ = ['\"]([^'\"]+)['\"]$", line)
            if res:
                return res.group(1)

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), 'r') as fd:
    long_description = fd.read()


if __name__ == '__main__':
    setup(
        name=pkg_name,
        version=get_version('src', pkg_name),
        description=description,
        long_description=long_description,

        # Author details
        author=author,
        author_email=author_email,

        # The project's main homepage.
        url=git_url,

        license='MIT',

        packages=find_packages(where='src'),
        package_dir={'':'src'},
        include_package_data=True,

        install_requires=[
            'numpy',
        ],
        zip_safe=False
    )