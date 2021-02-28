import sys
#Function to read a file and display the number of e's in a file
def checkFile(filename): #Function takes in the filename

    file = open(filename, 'r') #Open the file for reading
    file = file.read()
    e_count = 0 #Variable for the number of e's counted

    #Iterate through the file and for every e found, increase the count by one
    for letter in file:
        if 'e' in letter:
            e_count += 1
    return e_count

print(checkFile(sys.argv[1])) #Print the function which takes in a system argument 
                              #allowing for any existing filename to be called in the command line