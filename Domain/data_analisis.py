
def get_sum_distances(dict_gps_data):
    print("Distance:")
    for matricula, gps_data in dict_gps_data.items():
        print(matricula, " --> ", gps_data.sum_of_distances())




def get_sum_distances_with_lat_lon(dict_gps_data):
    # https://es.martech.zone/calculate-great-circle-distance/
    # https://community.fabric.microsoft.com/t5/Desktop/How-to-calculate-lat-long-distance/td-p/1488227
    print("Distance with lat and lon:")
    for matricula, gps_data in dict_gps_data.items():
        print(matricula, " --> ", gps_data.sum_of_distances_lat_lon())


def get_sum_distances_with_lat_lon2(dict_gps_data):
    # https://es.martech.zone/calculate-great-circle-distance/
    # https://community.fabric.microsoft.com/t5/Desktop/How-to-calculate-lat-long-distance/td-p/1488227
    print("Distance with lat and lon 2:")
    for matricula, gps_data in dict_gps_data.items():
        print(matricula, " --> ", gps_data.sum_of_distances_lat_lon2())



