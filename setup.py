#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

setup(
    author="Stefan Davis",
    author_email="stef.mdavis96@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    dependency_links=[],
    description="Modular Python framework that allows you to design, test, and evaluate various trading strategies using historical financial data.",
    install_requires=[],
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="trading_strat_backtester",
    name="trading_strat_backtester",
    packages=find_packages(include=["trading_strat_backtester*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/anmut-consulting/trading_strat_backtester",
    version="0.0.1",
    zip_safe=False,
)
