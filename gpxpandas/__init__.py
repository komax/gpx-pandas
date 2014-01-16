__author__ = 'max'

import gpxpandas.gpxreader as gpx_reader


def read_gpx_file(gpx_file_name):
    with open(gpx_file_name, 'r') as gpx_file:
        gpx = gpx_reader.parse_gpx(gpx_file)
        return read_gpx(gpx)


def read_gpx(gpx):
    return gpx_reader.pandas_data_frame_for_gpx(gpx)


def write_gpx(pd_data_frame):
    # TODO write gpx file from pandas
    pass