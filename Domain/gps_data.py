import math


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

    def sum_of_distances_lat_lon(self):
        # https://es.martech.zone/calculate-great-circle-distance/
        # https://community.fabric.microsoft.com/t5/Desktop/How-to-calculate-lat-long-distance/td-p/1488227
        r = 6371.0  # Earth radious
        total_distance = 0
        for i in range(1, len(self.list_latitud)):

            lat1, lon1 = self.list_latitud[i - 1], self.list_longitud[i - 1]
            lat2, lon2 = self.list_latitud[i], self.list_longitud[i]

            lat1_rad = math.radians(lat1)
            lon1_rad = math.radians(lon1)
            lat2_rad = math.radians(lat2)
            lon2_rad = math.radians(lon2)

            # Haversine formula
            diff_lat = lat2_rad - lat1_rad
            diff_lon = lon2_rad - lon1_rad
            a = math.sin(diff_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(diff_lon / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = r * c

            total_distance += distance

        return total_distance

    def last_date(self):
        return max(self.list_pos_date)  # Obtain the bigger pos_date of the list

