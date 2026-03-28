from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fitsms",
    version="1.0.2",
    author="Danuja Dilanka",
    author_email="dilanka.rajapakshe1@gmail.com",
    description="Official Python SDK for FitSMS.lk Gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Global-Cloud-Media-Pvt-Ltd/fitsms-python-sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests>=2.25.1"],
    python_requires='>=3.6',
)