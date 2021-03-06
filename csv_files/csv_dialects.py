import csv

# with open('passwd', 'r') as f:
#     reader = csv.reader(f, delimiter = ':', lineterminator='\n')
#
#     for row in reader:
#         print(row)
#
#         # A dialect describes the properties of a csv file
# print(csv.list_dialects())

# with open('items.csv', 'r') as f:
#     reader = csv.reader(f, delimiter = '#', lineterminator='\n')
#
#     for row in reader:
#         print(row)

csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')
with open('items.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='hashes')

    for row in reader:
        print(row)

with open('items.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, dialect='hashes')
    writer.writerow(('spoon', 3, 1.5))
