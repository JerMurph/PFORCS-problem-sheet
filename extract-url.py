import re

#This function extracts the query parameters from the URL's in an access.log file and stores them in a list. 
#They are also then split apart into either a resource or parameter and stored into
def extractURL():

    #Initialize blank variables for the list and dicts
    urls = []
    urlDict = {}
    parameterDict = {}
    urlCount = 0

    try:
        with open("access.log", 'r') as logFile: #Open the file for reading 
            for line in logFile:
                url = re.findall('(?:(GET|POST) )(\S+)', line)[0][1] #Get all the query parameters from every URL
                urls.append(url)   #Add them to the list

                #Split up the url from the ? and the parameters by the &
                urlPath = re.split('\?', url)[0]
                urlParameters = re.split('\?', url)[1]
                urlParameter = re.split('&', urlParameters)

                #Iterate through all the keys and values and add them to the dict
                for i in urlParameter:
                    key = re.split('=', i)[0]
                    value = re.split('=', i)[1]
                    parameterDict[key] = value
                urlDict[urlCount] = {'resource': urlPath, 'parameters': parameterDict}
                urlCount += 1
        print(urls) #Prints out the unaltered url parameters
        print(urlDict) #Prints out the split url parameters
    except FileNotFoundError:
        print("Cannot find the file")

extractURL()