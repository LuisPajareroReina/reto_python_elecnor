

class GpsData:

    def __init__(self, matricula):
        self.matricula = matricula
        self.list_latitud = []
        self.list_longitud = []
        self.list_distance = []
        self.list_pos_date = []

    def add_gps_data(self, latitud, longitud, distance, pos_date):
        self.list_latitud.append(latitud)
        self.list_longitud.append(longitud)
        self.list_distance.append(distance)
        self.list_pos_date.append(pos_date)


    def sum_of_distances(self):
        return sum(self.list_distance)