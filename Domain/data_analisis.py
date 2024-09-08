from datetime import datetime


def get_sum_distances(dict_gps_data):
    print("Distance (distance used):")
    for matricula, gps_data in dict_gps_data.items():
        print(matricula, " --> ", gps_data.sum_of_distances())


def get_sum_distances_with_lat_lon(dict_gps_data):
    # https://es.martech.zone/calculate-great-circle-distance/
    # https://community.fabric.microsoft.com/t5/Desktop/How-to-calculate-lat-long-distance/td-p/1488227
    print("Distance (lat and lon used):")
    for matricula, gps_data in dict_gps_data.items():
        print(matricula, " --> ", gps_data.sum_of_distances_lat_lon())


def get_last_dates(dict_gps_data):
    dates_dict = {}
    for matricula, gps_data in dict_gps_data.items():
        dates_dict[matricula] = gps_data.last_date()

    # sort dict by pos_date
    # https://blogboard.io/blog/knowledge/python-sorted-lambda/
    sort_date_dict = sorted(dates_dict.items(), key=lambda item: item[1], reverse=True)

    # print(posix_to_date(sort_date_dict))
    new_date_format_list = posix_to_date(sort_date_dict)

    return new_date_format_list



def posix_to_date(posix_dates_dict):
    new_date_dict_format = {}
    for matricula, date in posix_dates_dict:

        new_date = datetime.utcfromtimestamp(date / 1000)  # from posix to datetime
        new_format = new_date.strftime("%d/%m/%Y %H:%M:%S")  # using the power of datetime
        new_date_dict_format[matricula] = new_format

    return new_date_dict_format


