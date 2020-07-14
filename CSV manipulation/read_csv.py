import csv

csv_file = '../CSV manipulation/resource/mpg.csv'


def read_csv(file_name):
    print("reading from csv file ..." + file_name)
    with open(file_name) as file_object:
        return list(csv.DictReader(file_object))


csv_as_dictionary = read_csv(csv_file)

print("length of csv -->" + str(len(csv_as_dictionary)))

print("header names -->" + str(csv_as_dictionary[0].keys()))

print("first 3 dictionary entry -->" + str(csv_as_dictionary[:3]))

# how to find the average cty fuel economy across all cars.

avrg_city_fuel_economy = sum(float(d['cty']) for d in csv_as_dictionary) / len(csv_as_dictionary)

print("average cty fuel economy -> " + str("{:.3f}".format(avrg_city_fuel_economy)))

# Use set to return the unique values for the number of cylinders the cars in our dataset have.

cylinders = set(d['cyl'] for d in csv_as_dictionary)

print(cylinders)

# grouping the cars by number of cylinder, and finding the average cty mpg for each group.

CtyMpgByCyl = []

for c in cylinders:

    summpg = 0
    cyltypecount = 0

    for d in csv_as_dictionary:
        if d['cyl'] == c:
            summpg += float(d['cty'])
            cyltypecount += 1
    CtyMpgByCyl.append((c, "{:.2f}".format(summpg / cyltypecount)))

CtyMpgByCyl.sort(key=lambda x: x[0])

print(CtyMpgByCyl)

# se set to return the unique values for the class types in our dataset.

vehicle_class = set(d['class'] for d in csv_as_dictionary)

print(vehicle_class)

# find the average hwy mpg for each class of vehicle in our dataset

averg_hgy_mpg = []

for vc in vehicle_class:
    sumhwympg = 0
    vc_type = 0
    for d in csv_as_dictionary:
        if d['class'] == vc:
            sumhwympg += float(d['hwy'])
            vc_type += 1
    averg_hgy_mpg.append((vc, "{:.2f}".format(sumhwympg / vc_type)))

averg_hgy_mpg.sort(key=lambda x: x[0])

print(averg_hgy_mpg)
