import json


class GpsData:
    def __init__(self ,matricula ,latitud ,longitud ,distance ,pos_date):
        self.matricula = matricula
        self.latitud = []
        self.longitud = []
        self.distance = []
        self.pos_date = []
        self.data = {'Matricula': matricula,
              'Latitud': latitud,
              'Longitud': longitud,
              'Distance': distance,
              'Pos_date': pos_date
              }
