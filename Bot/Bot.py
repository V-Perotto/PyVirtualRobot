import os
import shutil
from Resource.Settings import ROOT
from Task.Task import task
import argparse

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Just an example",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("template_name", help="Source location")
    args = parser.parse_args()
    config = vars(args)
    print(config)
    # shutil.copytree(ROOT, os.path.join(ROOT, config["template_name"]))