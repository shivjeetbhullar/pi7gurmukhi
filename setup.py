import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pi7gurmukhi", 
    version="0.1.0",
    author="Shivjeet Singh Bhullar",
    author_email="bhullarshivjeet@gmail.com",
    description="Helpful In Write Correct Punjabi/Gurmukhi On Images, Pdf, Kivy & Others.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shivjeetbhullar/gurmukhi",
    packages=setuptools.find_packages(),
    package_data={'fonts': ['*']},
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Natural Language :: Panjabi",
        "Programming Language :: Python",
        "Topic :: Text Processing :: Fonts"

    ],
    python_requires='>=3',
)
