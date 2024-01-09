import json

from api.utils.paths import Paths


class Processor:
    def __init__(self):
        self.paths = Paths()

    # Fun for reprocessing response fro index model
    def reproccess_response_index(self, response):
        res2 = str(response)
        # re-processing from agent_chain ans:
        if res2.find('{\'answer\':') >= 0:
            res2 = res2.split('{\'answer\':')[1].split('\', \'sources\':')[0]
        if res2.find('Canned:') >= 0:
            res2 = res2.split('Canned:')[1]
        if res2[0] == ' ':
            res2 = res2[1:]
            while res2[0] == ' ':
                res2 = res2[1:]
        res2 = res2.replace('\n', '')
        res2 = res2.replace('. ', '.\n')
        return res2

    # split json new data to name data & new data for add and train index model
    def split_new_data_for_retrain(self, new_data_json):
        name_data = new_data_json['name_data']
        new_data = new_data_json['new_data']
        return name_data, new_data

    #  save new data to json file in docs
    def save_to_json_file(self, name_file, data, path):
        # read data
        ini_string = json.dumps(data)
        print('data : ', data)
        j = json.loads(ini_string)
        # save new data in json file in path
        with open(f'./{path}/{name_file}.json', 'w', encoding='utf-8') as f:
            json.dump(j, f, ensure_ascii=False, indent=4)
        f.close()
