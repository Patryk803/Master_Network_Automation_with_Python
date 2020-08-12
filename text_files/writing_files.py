with open('newfile.txt', 'w') as f: ## If the file doesn't exist the script will create it, it doesn't append in case the file is already created
    f.write('abc\n') # \n in order to move to the 2nd line
    f.write('just a 2nd line\n')

with open('newfile.txt', 'a') as f: ## Append to add to the existing file, but if it's not created it will create it
    f.write('Adding this at the end of the file')


with open ('newfile.txt', 'r+') as f:  ## r+ to get read and write permissions, it always writes from the beginning of the file

    f.write('Line added with r+')
