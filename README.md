# Rptree
Generates overviews of the structures of file directories. Example:
```
root_example\
├── example_dir_0\
│   ├── example_dir_00\
│   ├── example_dir_01\
│   └── example_file_00.txt
├── example_dir_1\
│   └── example_dir_10\
│       └── example_dir_100\
└── example_file_0.txt
```

## Installation
Make sure you have Python installed. Clone the repo and navigate to the location of the repo with a Python-ready terminal, and run `pip install .` when in the root of the repo. This will install the tool and enable its usage from any Python-ready terminal. 

## Usage
There are various modes of using this tool. The base usage looks like this:
```
tree-cli [-d] [-o output-file] path/to/file
```
Using the `-d` flag switches the tool to *directory-only* mode. Using the `-o` flag requires an additional argument of a markdown output file `output_file.md`. This then generates a markdown version of the same tree, ready to be used as needed. These flags are usable independently.

## License

[MIT](https://choosealicense.com/licenses/mit/) license, Copyright © 2025 Rens van Eck.