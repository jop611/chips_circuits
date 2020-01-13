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
    
    # iterate over coordinates
    while coordinates in paths:
        coordinates = paths[coordinates]
        path.append(coordinates)
        path.reverse()
    return path

    