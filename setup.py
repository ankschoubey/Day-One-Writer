import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dayonewriter",
    version="1.0",
    author="Ankush Choubey",
    author_email="ankushchoubey@outlook.com",
    description="Python wrapper which internally uses dayone-cli. Compatible with Day One 2+.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ankschoubey/dayonewriter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


