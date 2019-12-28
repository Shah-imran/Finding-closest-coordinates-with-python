import pickle
import csv
import time

with open('pythonTask.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    places = []
    storeP = []
    for row in csv_reader:
        temp = [int(row['Element ID']),(float(row['Latitude']), float(row['Longitude']))]
        places.append(temp)

temp = places
for i in temp:
    count = 0
    for j in range(len(places)-1):
        # print("Before-", j, len(places))
        # print(i[1][0], places[j][1][0], i[1][1], places[j][1][1])
        try:
            if i[1][0] == places[j][1][0] and i[1][1] == places[j][1][1]:
                # print("Matched")
                if count > 0:
                    places.pop(j)
                    # print(len(places), j, count)
                    j-=1
                    
                count+=1
        except:
            pass
    print(len(places))

with open('parrot.pkl', 'wb') as f:
    pickle.dump(places, f)