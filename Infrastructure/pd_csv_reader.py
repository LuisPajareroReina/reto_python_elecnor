import json
import pandas as pd
from Infrastructure.json_reader import JsonHandler


class PandasCsvHandler:

    def __init__(self, path):
        self.path = path
        self.csvfile = None

    def pandas_read_csv(self):
        self.csvfile = pd.read_csv(self.path)

    def print_csv(self, console=True):
        for index, row in self.csvfile.iterrows():
            if console:
                print(row)

    def csv_to_json(self, console=True):
        for index, row in self.csvfile.iterrows():
            line = row.to_dict()  # JSON need dictionary structure

            json_line = json.dumps(line, indent=5)  # the indent = 5 is for see the data clearly
            if console:
                print(json_line)

            # Save each line into a json using the index as ID
            json_name = 'Json_data/' + str(index) + '.json'
            jsonReader = JsonHandler(json_name)
            jsonReader.save_json(line)
