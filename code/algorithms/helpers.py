"""
Traces path of a connection coordinate by coordinate

(C) 2020 Teamname, Amsterdam, The Netherlands
"""

def trace(paths, destination):
    """ Returns a list of all passed coorinates """

    coordinates = destination
    path = [coordinates]
    print(f"Destination: {destination}")

    # iterate over coordinates
    while coordinates in paths:
        coordinates = paths[coordinates]
        path.append(coordinates)
    path.reverse()
    return path

def matlib_convert(path):
    """ Make coordinate list for matlib """
    
    x_list = []
    y_list = []
    z_list = []

    for coordinate in path:
        x_list.append(coordinate[0])
        y_list.append(coordinate[1])
        z_list.append(coordinate[2])
    return (x_list, y_list, z_list)
