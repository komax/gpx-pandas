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


def track_segment_mapping(track):
    segments = [ data_frame_for_track_segment(segment)
                 for segment in track.segments ]
    return segments


def pandas_data_frame_for_gpx(gpx):
    tracks_frames = [track_segment_mapping(track) for track in gpx.tracks]
    tracks_frame = pd.DataFrame(tracks_frames)
    return tracks_frame