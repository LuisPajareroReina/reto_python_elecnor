from flask import Flask

from Infrastructure.pd_csv_reader import PandasCsvHandler
from Infrastructure.json_reader import JsonHandler
from Infrastructure.txt_reader import TxtHandler
from Infrastructure.sql_handler import SqlHandler
from Domain.data_analisis import get_sum_distances, get_sum_distances_with_lat_lon, get_last_dates

CSV_PATH = "Data/reto.csv"
JSON_PATH = "Json_data/"
TXT_PATH = "Txt_data/reto 5.txt"
SQL_FILE_PATH = "init.sql"
CONSOLE = False

CASO_1 = False
CASO_2 = False
CASO_3 = False
CASO_4 = False
CASO_5 = False
CASO_6 = False
CASO_7 = True

# CASO 1. Empezamos por algo fácil: Lee el fichero CSV
# e imprime cada línea
if CASO_1:
    pandasCsvReader = PandasCsvHandler(CSV_PATH)
    pandasCsvReader.pandas_read_csv()
    pandasCsvReader.print_csv(CONSOLE)

# CASO 2. Lee el fichero CSV, convierte cada línea a un
# JSON e imprímelo.
if CASO_2:
    pandasCsvReader.csv_to_json(CONSOLE)

# CASO 3. Subimos de dificultad: En cada fila se incluye
# la distancia que el vehículo ha recorrido con respecto
# a su posición anterior. Calcula el sumatorio de las
# distancias de cada vehículo, usando el campo
# "distancia" a partir del formato json. Imprime todos
# los resultados por consola.
if CASO_3:
    jsonReader = JsonHandler(JSON_PATH)
    jsonReader.read_json()

    get_sum_distances(jsonReader.dict_gps_data)

# CASO 4. Esto se complica: Ahora calcula el sumatorio
# de distancias de cada matrícula, usando las
# coordenadas geográficas (el cálculo debe hacerse a
# partir del formato json) e imprime todos los resultados
# por consola.
if CASO_4:
    get_sum_distances_with_lat_lon(jsonReader.dict_gps_data)

# CASO 5. ¿Listo? Escribe un nuevo fichero de texto
# donde aparezca la fecha de la última posición de cada
# vehículo en formato (dd/mm/YYY HH:MM:SS) a partir
# del campo "pos_date". Recuerda, pos_date es una
# fecha en Tiempo POSIX. Escribe el fichero ordenado
# por fecha, de la más reciente a la más antigua.
if CASO_5:
    last_dates_dict = get_last_dates(jsonReader.dict_gps_data)
    txtReader = TxtHandler(TXT_PATH)
    txtReader.dict_to_txt(last_dates_dict)

# CASO 6. Ahora Crea un API REST con un método GET
# del estilo (http://localhost/XXX) dónde XXX es la
# matrícula de un vehículo. Su resultado debe leerse del
# fichero del punto anterior y devolver la fecha de
# última posición de la matrícula indicada
if CASO_6:
    # https://www.youtube.com/watch?v=b0ZrmhyyCY4&ab_channel=JavierPinilla
    app = Flask(__name__)

    txtReader.read_txt()

    @app.route('/<matricula>', methods=['GET'])
    def get_last_date_with_api(matricula):
        if matricula in txtReader.dict_pos_date:
            pos_date = txtReader.dict_pos_date[matricula]
            return pos_date

        return "Error/Not found"


    if __name__ == '__main__':
        app.run(debug=True)

# CASO 7. ¿Te atreves a levantar un contenedor Docker
# con una base de datos e incluir en ella los datos del
# fichero del punto 5?
if CASO_7:
# https://dev.to/marlosrodriguez/crear-contenedores-de-bases-de-datos-en-docker-bdg
# https://www.youtube.com/watch?v=kWHWg8Oj5-Y&ab_channel=DebuggeandoIdeas

    sqlHandler = SqlHandler(SQL_FILE_PATH)
    sqlHandler.create_table_from_txt(TXT_PATH)



