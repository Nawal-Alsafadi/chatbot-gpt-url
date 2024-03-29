import importlib.util
import os
import pkg_resources
import subprocess
import sys
import importlib.util
import yaml


class FirstInit:
    def __init__(self):
        self.requirements = [['llama_index', '0.6.6'], ['langchain', '0.0.167'],
                             ['flask', '2.3.2'], ['flask_cors', '3.0.10']]
        # , ['sklearn', '1.0.2', 'scikit-learn'],
        #                      ['texthero', '1.1.0'], ['scipy', '1.10.1'], ['tensorflow', '2.12.0'],
        #                      ['opencv-python', '4.7.0.72'],['mlxtend','0.22.0'],['scikit-surprise','1.1.3']]

    def get_requirements(self):
        return self.requirements

    def install(self, package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    def check_requirements(self):
        for req in self.get_requirements():
            spec = importlib.util.find_spec(req[0])
            if spec is None:
                print(f"{req[0]!r} not in sys.modules")
                print(f'wait {req[0]}=={req[1]}  will downloaded now !!!')
                self.install(f'{req[0]}=={req[1]}')
                print(f'complete download {req[0]}=={req[1]} !!!!!!!')

            else:
                if req[0] == 'sklearn':
                    package_version = pkg_resources.get_distribution(req[2]).version
                else:
                    package_version = pkg_resources.get_distribution(req[0]).version
                if not (package_version == req[1]):
                    print(f"{req[0]!r} not same version, version: {package_version} !!!!")
                    print(f'wait {req[0]}=={req[1]}  will downloaded now !!!')
                    self.install(f'{req[0]}=={req[1]}')
                    print(f'complete download {req[0]}=={req[1]} !!!!!!!')
                else:
                    print(f"{req[0]!r} already in sys.modules")

    # get openai_key from secret path
    # def get_api_key(self):
    #     api_key = "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"
    #     with open("api_key.yaml", "r") as stream:
    #         try:
    #             api_key = yaml.safe_load(stream)
    #         except yaml.YAMLError as exc:
    #             api_key = exc

        # return api_key
    def get_api_key(self):
        api_key = self.get_api_key_from_yaml()
        return api_key
    def get_api_key_from_yaml(self, file_name="api_key.yaml"):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, file_name)
        try:
            with open(file_path, "r") as stream:
                yaml_data = yaml.safe_load(stream)
                if yaml_data is not None and isinstance(yaml_data, dict) and "api_key" in yaml_data:
                    api_key = yaml_data["api_key"]
                    if isinstance(api_key, str):
                        return api_key
                    else:
                        raise ValueError("Invalid API key format in the YAML file.")
                else:
                    raise ValueError("Invalid YAML file structure.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The YAML file '{file_path}' was not found.")
        except yaml.YAMLError as exc:
            raise ValueError(f"Error loading API key from YAML file: {exc}")

    

