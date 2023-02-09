from setuptools import setup, find_packages


setup(
    name="adrian",
    version="0.0.1",
    license="MIT",
    author="Adrian Tam",
    author_email="email@example.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/gmyrianthous/example-publish-pypi",
    keywords="example project",
    install_requires=[
        "scikit-learn",
    ],
)
