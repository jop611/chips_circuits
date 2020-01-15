def trace(paths, destination):
    """
    Traces path of a connection coordinate by coordinate

    Inputs
    paths: a dictionary containing destination-coordinates as keys 
           with origin-coordinates as values

    destination: first set of coordinates (tuple)
           

    Returns a list of all passed coorinates
    """ 


    coordinates = destination
    path = [coordinates]
    print(f"Destination: {destination}")
    # iterate over coordinates
    while coordinates in paths:
        # print(f"New: {coordinates}")
        # print(f"Origin: {paths[coordinates]}")
        coordinates = paths[coordinates]
        path.append(coordinates)
    path.reverse()
    return path
    

def matlib_convert(path):
    x_list = []
    y_list = []
    z_list = []
   
    for coordinate in path:
        x_list.append(coordinate[0])
        y_list.append(coordinate[1])
        z_list.append(coordinate[2])
    return (x_list, y_list, z_list)

    