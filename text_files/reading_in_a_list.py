# with open('configuration.txt') as file:
#     my_list = file.read().splitlines()
#     print(my_list)

# with open('configuration.txt', 'r') as file:
#     my_list = file.readlines()    ## Here after every line we will se \n which indicates new line
#     print(my_list)

# with open('configuration.txt', 'r') as file:
#     my_list = file.read().splitlines()
#     print(my_list)
#
# with open('configuration.txt', 'r') as file:
#     print(file.readline())  ## Read line is to read just one line - not the entire file
#     print(file.readline())
#
with open('configuration.txt', 'r') as file:
    for k in file:
        print(k, end='')  ## end to don't get empty lines between commands
