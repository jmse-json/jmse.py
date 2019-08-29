#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="jmse",
    version="0.0.0",
    description="JSON Message Signing and Encryption (JMSE)",
    long_description="An interoperable, minimalist signing and encryption format for JSON messages.",
    author="Tony Arcieri",
    author_email="tony@iqlusion.io",
    url="https://github.com/jmse-json/jmse.py",
    packages=["jmse"],
    package_dir={"jmse": "jmse"},
    include_package_data=True,
    install_requires=[],
    license="Apache Software License",
    keywords=["json", "encryption", "signing", "serialization"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
    ],
    test_suite="tests",
    tests_require=[]
)
