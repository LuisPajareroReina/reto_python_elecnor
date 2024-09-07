import json
import os

from Domain.gps_data import GpsData


class JsonReader:

    def __init__(self, path):
        self.path = path
        self.dict_gps_data = {}  # Dictionary with all the data of each matricula

    def read_json(self):
        # https://j2logo.com/python/listar-directorio-en-python/#:~:text=Para%20listar%20o%20recorrer%20un,archivos%20y%20carpetas%20que%20contiene.
        num_unico_matriculas = 0
        for name in os.listdir(self.path):
            file_path = os.path.join(self.path, name)

            # Read each json file
            with open(file_path) as json_path:
                # https://www.freecodecamp.org/espanol/news/python-leer-archivo-json-como-cargar-json-desde-un-archivo-y-procesar-dumps/
                data = json.load(json_path)

                matricula = data['Matricula']
                latitud = float(data['Latitud'])
                longitud = float(data['Longitud'])
                distance = float(data['Distance'])
                pos_date = int(data['Pos_date'])

                if matricula in self.dict_gps_data:
                    self.dict_gps_data[matricula].add_gps_data(latitud, longitud, distance, pos_date)
                else:
                    gps_data = GpsData(matricula)
                    gps_data.add_gps_data(latitud, longitud, distance, pos_date)
                    self.dict_gps_data[matricula] = gps_data
                    num_unico_matriculas += 1

        print("Número único de matriculas: ", num_unico_matriculas)

    def save_json(self, data):
        with open(self.path, 'w') as json_file:
            json.dump(data, json_file, indent=5)
