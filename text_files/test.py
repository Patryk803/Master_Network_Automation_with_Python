import os
print (os.getcwd()) ## prints current working directory

#print() ## gives an empty line in the output

f = open('configuration.txt', 'r') ### We have 3 modes read, write, append

## End of line is encoded as /n

content = f.read(3)   ## Python stopped the cursor at letter 's'
print(content)
print(f.tell())              ## Prints the currrent position of the cursor
                            ## To print the whole config file we would need to leave f.read() blank
content = f.read(3)
print(content)

f.seek(2)   ## Moves the cursor to position 2 which is 's'
print(f.read(1)) ##reads 2 so from s to t

#
# hej = f.read(2) ## That one will print first 5 characters
# print(content)

print(f.closed) ##Otput FALSE would mean that file is still open
f.close() ## Closing the file - Always remember to close the file after using it
print(f.closed) ## Output TRUE would mean that the file is closed
