import os
import json
from typing import Optional
from Resource.Settings import INPUT_PATH, OUTPUT_PATH

class JSON():

    def __init__(self) -> None:
        pass

    def __validate_json_name(self, filename: str) -> str:
        if not '.json' in filename[-5:]:
            filename = f"{filename}.json"
        return filename

    def read(self, filename: str, json_file_path: Optional[str] = INPUT_PATH):
        """Read a .json file. \n
            - OPTIONAL = Default path is from Input directory.
        """
        try:
            with open(os.path.join(json_file_path, self.__validate_json_name(filename)), "r") as openfile:
                json_obj = json.load(openfile)
            return json_obj
        except Exception as e:
            raise e     # f'Error to read a JSON file. \n{e}' 

    def write(self, filename: str, dict_package: dict, json_file_path: Optional[str] = OUTPUT_PATH):
        """Write a .json file. \n
            - OPTIONAL = Default path is from Output directory. 
        """
        try:
            with open(os.path.join(json_file_path, self.__validate_json_name(filename)), "w") as outfile:
                json.dump(dict_package, outfile)       
            return True
        except Exception as e:       
            raise e     # f'Error to write a JSON file. \n{e}'
        
JsonLib = JSON()