from setuptools import setup, find_packages

setup(
    name = "rptree",
    version = "0.2.0",
    packages = find_packages(),
    install_requires = [],
    entry_points={
        "console_scripts": [
            "tree-cli=rptree.tree:main",
        ],
    },
    description = "A python package to create project tree structures",
    author = "Rens van Eck",
    author_email = "rensvaneck@gmail.com",
    url = "https://github.com/Renseck/rp_tree",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",        
    ],
)