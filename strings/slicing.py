# Strings are immutable so if we have a string = woda, we cannot change it's first letter by string[o] = p

movie = 'The Godfather'

print(movie[0:2]) # First letter is always included while the last is excluded

# We can get the whole string by

print(movie[0:1] + movie[1:])

#Last 3 to the end by:

print(movie[-3:])

## with slicing we can use out of boundary parameters

print(movie[4:555]) # but print(movie[555]) wouldn't work

print(movie[90:]) # This will return an empty string

print(movie[0:10:2]) # 0 to 10 in steps of 2

print(movie[10:6:-1]) # It will start from the end to the beginning
