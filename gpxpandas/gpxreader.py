__author__ = 'max'

import gpxpy
import pandas as pd


def parse_gpx(gpx_file_name):
    return gpxpy.parse(gpx_file_name)


def data_frame_for_track_segment(segment):
    seg_dict = {}

    for point in segment.points:
        seg_dict[point.time] = [point.latitude, point.longitude, point.elevation]
    dframe = pd.DataFrame(data=seg_dict)
    # Switch columns and rows s.t. timestamps are rows and gps data columns
    dframe = dframe.T
    dframe.columns = ['latitude', 'longitude', 'altitude']
    return dframe