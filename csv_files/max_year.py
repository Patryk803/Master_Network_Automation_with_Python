import csv

with open('airtravel.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # To skip the first line of the columns
        year_1958 = dict()
        for row in reader:
            year_1958[row[0]] = row[1] # It basically faces months with the values from year 1958

        print(year_1958)

        max_1958 = max(year_1958.values())
        print(max_1958)
