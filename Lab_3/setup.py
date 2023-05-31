from setuptools import find_packages, setup

setup(
    name="argo",
    version="0.1.1",
    packages=find_packages(include=["argo", "argo.*"]),
    description="XML & JSON serialization tools at BSUIR 2023 spring semester.""",
    author="Me",
    license="MIT",
    entry_points={
        'console_scripts': ['argo=argo.lib:main']
    }
)