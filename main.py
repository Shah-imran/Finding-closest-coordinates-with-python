from scipy import spatial
import csv
import math
import threading
import queue, time

q = queue.Queue()
storeP = []

def cartesian(latitude, longitude, elevation = 0):
    # Convert to radians
    # print(type(latitude), type(math.pi / 180))
    latitude = latitude * (math.pi / 180)
    longitude = longitude * (math.pi / 180)

    R = 6371 # 6378137.0 + elevation  # relative to centre of the earth
    X = R * math.cos(latitude) * math.cos(longitude)
    Y = R * math.cos(latitude) * math.sin(longitude)
    Z = R * math.sin(latitude)
    return (X, Y, Z)

def savingCsv():
    csv_columns = ['Element_ID_Source','Latitude_Source','Longitude_Source', 'Element_ID_target', 'Latitude_target', 'Longitude_target']
    csv_file = 'output.csv'
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        dict_data = dict()
        while True:
            if not q.empty():
                data = q.get()
                # print(data[1], data[0])
                for j in data[1]:
                    if storeP[j][0] != data[0][0]:
                        dict_data[csv_columns[0]] = data[0][0]
                        dict_data[csv_columns[1]] = data[0][1][0]
                        dict_data[csv_columns[2]] = data[0][1][1]
                        dict_data[csv_columns[3]] = storeP[j][0]
                        dict_data[csv_columns[4]] = storeP[j][1][0]
                        dict_data[csv_columns[5]] = storeP[j][1][1]
                        writer.writerow(dict_data)
                        print(dict_data)


# threading.Thread(target=savingCsv, daemon=False).start()

with open('pythonTask.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    places = []
    for row in csv_reader:
        # arranging
        
        coordinates = [float(row['Latitude']), float(row['Longitude'])] # list
        temp = [int(row['Element ID']),(float(row['Latitude']), float(row['Longitude']))] 
        cartesian_coord = cartesian(*coordinates)
        places.append(cartesian_coord)
        storeP.append(temp)


print(len(places))
print("Fitting Data -")
tree = spatial.cKDTree(places)
count = 0

resultP = []
print(count)
coordinates = [28.025631, -82.440425]
result = tree.query(cartesian(*coordinates), k=21)
# print("Results - ")
print(result)
print(storeP[148982])
if len(result[1]) < 21 or len(result[1]) > 21:
    print("case detected")
    time.sleep(10)
resultP.append([storeP[84687],result[1]])
count+=1
for i in result[1]:
    print(storeP[i])
print("Total Rows-")    
print(len(resultP))
time.sleep(5)
csv_columns = ['Element_ID_Source','Latitude_Source','Longitude_Source', 'Element_ID_target', 'Latitude_target', 'Longitude_target']
csv_file = 'output1.csv'
count = 0
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    dict_data = dict()
    for data in resultP:
        for j in data[1]:
            if storeP[j][0] != data[0][0]:
                print(count)
                dict_data[csv_columns[0]] = data[0][0]
                dict_data[csv_columns[1]] = data[0][1][0]
                dict_data[csv_columns[2]] = data[0][1][1]
                dict_data[csv_columns[3]] = storeP[j][0]
                dict_data[csv_columns[4]] = storeP[j][1][0]
                dict_data[csv_columns[5]] = storeP[j][1][1]
                writer.writerow(dict_data)
                count+=1
                print(dict_data)
print("finished")