import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="netra-client-python",
    version="0.1.1",
    author="Paitoon C.",
    author_email="paitoon.chw@gmail.com",
    description="Python Client Library for Netra.AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paitoon/netra.ai-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
)
