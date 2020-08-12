import csv

with open('airtravel.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # To skip the first line of the column
        for row in reader:
            #print(row)
            print(row[2]) # To print 3rd column
