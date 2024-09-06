from Infrastructure.pd_csv_reader import PandasCsvReader
from Infrastructure.json_reader import JsonReader
from Domain.data_analisis import get_sum_distances
CSV_PATH = "Data/reto.csv"
JSON_PATH = "Json_data/"

# CASO 1. Empezamos por algo fácil: Lee el fichero CSV
# e imprime cada línea
pandasCsvReader = PandasCsvReader(CSV_PATH)  # Create the object PandasCsvReader
pandasCsvReader.pandas_read_csv()  # Load the csv file
pandasCsvReader.print_csv()  # Print csv

# CASO 2. Lee el fichero CSV, convierte cada línea a un
# JSON e imprímelo.
pandasCsvReader.to_json()

# CASO 3. Subimos de dificultad: En cada fila se incluye
# la distancia que el vehículo ha recorrido con respecto
# a su posición anterior. Calcula el sumatorio de las
# distancias de cada vehículo, usando el campo
# "distancia" a partir del formato json. Imprime todos
# los resultados por consola.
jsonReader = JsonReader(JSON_PATH)
jsonReader.read_json()
get_sum_distances(jsonReader.dict_gps_data)

