### 1 approach ###

# with open('devices.txt', 'r') as f:
#     devices = f.read().splitlines()
#     #print(my_list)
#
# mylist = list() # Creates an empty list
#
# for item in devices:
#     tmp = item.split(':') # Colon as a delimiter
#     mylist.append(tmp)
#     print(tmp)


### 2 approach ###

import csv

with open('devices.txt') as f:
    reader = csv.reader(f, delimiter=':')      # reader object = reader method of a csv module
    for row in reader:
        print(row)


### 3 approach ###

import csv

with open('devices.txt') as f:
    reader = csv.reader(f, delimiter=':')      # reader object = reader method of a csv module
    mylist = list()
    for row in reader:
        mylist.append(row)

    print(mylist)
