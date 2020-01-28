"""
helpers.py

Traces path of a connection and appends coordinates to list used for visualisation.

(C) 2020 Teamname, Amsterdam, The Netherlands
"""

def trace(paths, destination):
    """Traces path from destination to origin"""

    coordinates = destination
    path = [coordinates]

    while coordinates in paths:
        coordinates = paths[coordinates]
        path.append(coordinates)
    path.reverse()
    return path


def matlib_convert(path):
    """Convert (x, y, z) coordinates to x-, y-, z- coordinate lists for visualisation via matplotlib"""

    x_list = []
    y_list = []
    z_list = []

    for coordinate in path:
        x_list.append(coordinate[0])
        y_list.append(coordinate[1])
        z_list.append(coordinate[2])
    return (x_list, y_list, z_list)
