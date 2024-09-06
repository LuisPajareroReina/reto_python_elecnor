import csv
import json
from Domain.gps_data import GpsData

# https://docs.python.org/es/3/library/csv.html
class CsvReader:

    def __init__(self, path):
        self.path = path
        self.csvfile = None

    def read_csv(self):
        self.csvfile = open(self.path)

    def print_csv(self):
        for row in self.csvfile:
            print(row)

    def to_json(self):
        # atributes = ['Matricula', 'Latitud', 'Longitud', 'Distance', 'Pos_date']

        # recorrer cada linea
        for row in self.csvfile:
            values = row.split(",")  # transform string to list
            print(values)
            gps_data = GpsData(values[0], values[1], values[2], values[3], values[4])
            gps_data.data.to_dict()  # JSON need dict structure

            json_line = json.dumps(gps_data.data, indent=5)

            print(json_line)


