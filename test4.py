import csv
# import pickle


# with open('parrot.pkl', 'rb') as f:
#     mynewlist = pickle.load(f)

#     print(len(mynewlist))


#     places = list(dict.fromkeys(places))

# with open('parrot.pkl', 'rb') as f:
#     placesL = pickle.load(f)
# print(len(placesL))

# places = []
# for row in placesL:
#     coordinates = [row[1][0], row[1][1]]
#     cartesian_coord = cartesian(*coordinates)
#     places.append(cartesian_coord)
with open('output.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    print(len(list(csv_reader)))