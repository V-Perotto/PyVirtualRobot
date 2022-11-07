import json

class lib_json:

    def read(self, filename):
        try:
            with open(filename, "r") as openfile:
                json_obj = json.load(openfile)
            return json_obj
        except Exception as e:
            return str(e) 

    def write(self, filename, dict_env):
        try:
            with open(filename, "w") as outfile:
                json.dump(dict_env, outfile)       
            return True
        except Exception as e:       
            return str(e) 