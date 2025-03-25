import argparse
import pathlib
import sys

from . import __version__
from .rptree import DirectoryTree

def parse_cli_args():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="RP Tree, a directory tree generator",
        epilog="Thanks for using RP Tree",
    )
    parser.version = f"RP tree v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir", 
        metavar = "ROOT_DIR",
        nargs = "?",
        default = ".",
        help = "Generate a full directory tree starting at ROOT_DIR"
    )
    
    return parser.parse_args()

# ==================================================================================================

def main():
    args = parse_cli_args()
    root_dir = pathlib.Path(args.root_dir)
    
    if not root_dir.is_dir():
        print("The specified root does not exist")
        sys.exit()
    
    tree = DirectoryTree(root_dir)
    tree.generate()