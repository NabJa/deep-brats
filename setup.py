import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deep-brats",
    version="0.0.1",
    author="Nabil Jabareen",
    author_email="nabil.jabareen@gmail.com",
    description="Deep learning for brats data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NabJa/deep-brats",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
