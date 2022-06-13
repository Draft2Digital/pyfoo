#!python
from pathlib import Path
from setuptools import setup, find_packages

setup(
    name="pyfoo",
    version="0.3.0+d2d.001",
    description="Python wrapper around the Wufoo API",
    long_description=Path(__file__).with_name("README.markdown").read_text(),
    license="MIT",
    keywords="python",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    packages=find_packages(),
    include_package_data=True,
)
