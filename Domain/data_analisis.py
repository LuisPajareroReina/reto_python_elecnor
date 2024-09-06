
def get_sum_distances(dict_gps_data):
    for matricula, gps_data in dict_gps_data.items():
        print(matricula, " --> ", gps_data.sum_of_distances())

