import csv

with open('airtravel.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # To skip the first row
        year_1958 = dict() # dictionary - Key-Value pairs ex: student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Physics']}
        for row in reader:
            year_1958[row[0]] = row[1] # It basically faces months with the values from year 1958

        print(year_1958)

        max_1958 = max(year_1958.values())
        print(max_1958)

        for k, v in year_1958.items():
            if 'AUG' == k:  ## max_1958 is the highest value so once it's stored in v we would print
                print(f'Busiest Month in 1958:{k}, Flights:{v.strip()}') #strip is a string method to get rid off white spaces due to csv file
