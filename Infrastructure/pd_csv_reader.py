import json

import pandas as pd


class PandasCsvReader:

    def __init__(self, path):
        self.path = path
        self.csvfile = None

    def pandas_read_csv(self):
        self.csvfile = pd.read_csv(self.path)

    def print_csv(self):
        for index, row in self.csvfile.iterrows():
            print(row)

    def to_json(self):
        for index, row in self.csvfile.iterrows():
            line = row.to_dict()  # JSON need dictionary structure

            json_line = json.dumps(line, indent=5)  # the indent = 5 is for see the data clearly
            print(json_line)

            # Save each line into a json using the index as ID
            json_name = 'Json_data/'+str(index) + '.json'
            with open(json_name, 'w') as json_file:
                json.dump(line, json_file, indent=5)



