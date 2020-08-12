# Create a Python script that reads a text file into a list and then converts the list back into a string which is the entire file content.

with open('sample_file.txt', 'r') as f:
    devices = f.read().splitlines()

mylist = list() # Creates an empty list

for item in devices:
    tmp = item.split('\n') # \n as a delimiter
    mylist.append(tmp)
    #print(tmp)

    my_str = '\n'.join(tmp)
    print(my_str)


### 2nd Method###

# with open('sample_file.txt', 'r') as f:
#     # reading the file in a list
#     content = f.read().splitlines()
#     # concatenating the list back into a string
#     my_str = '\n'.join(content)
#     print(my_str)
