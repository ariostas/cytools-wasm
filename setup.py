import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="cytools-wasm",
    version="0.0.1",
    author="Andres Rios Tascon",
    author_email="",
    description="A WebAssembly implementation of CYTools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ariostas/cytools-wasm",
    packages=setuptools.find_packages(),
    license="GNU General Public License (GPL)",
    python_requires='>=3.9',
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ]
)
