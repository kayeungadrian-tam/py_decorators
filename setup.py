from setuptools import setup, find_packages

# Parse the metadata from pyproject.toml
from pathlib import Path
import toml

metadata = toml.load(Path(__file__).parent / "pyproject.toml")["tool"]["poetry"]

# Define the package dependencies
dependencies = metadata["dependencies"]
requires = [f"{dep} {version}" for dep, version in dependencies.items()]

setup(
    name=metadata["name"],
    version=metadata["version"],
    description=metadata["description"],
    author=", ".join(author["name"] for author in metadata["authors"]),
    packages=find_packages(include=[metadata["packages"][0]["include"]]),
    license=metadata["license"],
    url=metadata["homepage"],
    install_requires=requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
