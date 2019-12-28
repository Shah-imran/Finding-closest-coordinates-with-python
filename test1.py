from sklearn.neighbors import NearestNeighbors
import numpy as np
import csv

def distance(p1, p2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    lon1, lat1 = p1
    lon2, lat2 = p2
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km

with open('pythonTask.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    places = []
    storeP = []
    for row in csv_reader:
        coordinates = [float(row['Latitude']), float(row['Longitude'])]
        temp = [int(row['Element ID']),(float(row['Latitude']), float(row['Longitude']))]
        # cartesian_coord = cartesian(*coordinates)
        places.append(coordinates)
        storeP.append(temp)
    places = list(dict.fromkeys(places))
    
    print(len(places))

# points = [[25.42, 55.47],
#           [25.39, 55.47],
#           [24.48, 54.38],
#           [24.51, 54.54]]

nbrs = NearestNeighbors(n_neighbors=2, metric=distance).fit(places)

distances, indices = nbrs.kneighbors(places)

result = distances[:, 1]

print(result)