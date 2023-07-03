import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="my-package",
    version="3.0",
    author="Dev",
    description="Demo package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
