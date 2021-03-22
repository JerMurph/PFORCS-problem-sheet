import pandas as pd
import re 
import matplotlib.pyplot as plt

fileName = 'access.log'

try:
    #Open up the file
    file = open(fileName, 'r', encoding='utf8')

    #Add column headers
    colNames= ('ip', 'dash', 'userID', 'time', 'url', 
           'status code', 'size of response', 'referer', 'user agent', 'dunno')

    #Read in the data from the file into a dataframe
    df = pd.read_csv(file, sep=' ', header= None, names=colNames)
    #Remove the [] from the time and covert the time into the datetime format
    df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())
    df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')
    #Set the datetime to be the index
    df = df.set_index(['time'])

    #Function to get the sessionID
    def getSessionID(x):
        #Get by using reg expressions to extraction the sessionID from the URL
        id = re.search('(JSESSIONID=\S+)', x).group()
        sessionID = re.split('=', id)[1]
        return sessionID

    df['sessionID'] = df['url'].apply(getSessionID)

    #Get the sum of all data downloaded using groupby
    print(df.groupby(by=['sessionID'])['size of response'].sum())

    #Plot a bar chart, again using the groupby data to plot it
    plotdata = df.groupby(by=['sessionID'])[['size of response']].sum()
    plotdata['size of response'].plot(kind="bar")

    #Axis labels
    plt.xlabel("Session ID")
    plt.ylabel("Data Downloaded")
    #Display the graph
    plt.show()

#File not found and/or doesn't exist
except FileNotFoundError:
    print("No file found")