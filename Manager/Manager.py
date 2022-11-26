import argparse, os, shutil, zipfile, io
from pathlib import Path

PACKAGE = Path(os.path.dirname(os.path.abspath(__file__)))  
CURDIR = os.getcwd() # Path(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":    
    desc = """This is a Manager to create a Bot Template"""
    parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("template_name", help="Set a name to your robot.")
    args = parser.parse_args()
    config = vars(args)
    shutil.copytree(os.path.join(PACKAGE, 'Bot'), os.path.join(CURDIR, config["template_name"]))

# python -m Manager.Manager -h