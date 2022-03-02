"""
https://packaging.python.org/tutorials/distributing-packages/
"""

import io
import os
import re

from setuptools import find_packages, setup

PKG_NAME = 'ferment_pi'
SRC_DIR = 'src'
BASEDIR = os.path.dirname(__file__)


def read(file_path):
    with io.open(file_path, 'r', encoding='utf-8') as fin:
        return fin.read()


def version():
    version_file_content = read(os.path.join(
        BASEDIR, SRC_DIR, PKG_NAME, '_version.py'))
    version_match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]',
                              version_file_content, re.M)
    if not version_match:
        raise RuntimeError('Unable to find version string.')
    return version_match.group(1)


setup(
    name=PKG_NAME,
    version=version(),
    keywords='',
    project_urls={},
    # http://setuptools.readthedocs.io/en/latest/setuptools.html#using-find-packages
    package_dir={'': SRC_DIR},
    packages=find_packages(SRC_DIR),
    package_data={
        # PKG_NAME: ["schema/*.json"],
    },
    data_files=[],
    install_requires=[
        "pillow",
        "sqlalchemy==1.4.23",
        "psycopg2",
        "alembic",
        "apscheduler",
        "fastapi",
        "uvicorn==0.15.0",
    ],
    extras_require={},
    python_requires=', '.join([
        '>=3.8',
        '<4',
    ]),
    entry_points={}
)
