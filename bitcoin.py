import json #import json module
import requests #import requests module

url = 'https://api.coindesk.com/v1/bpi/currentprice.json' #URL containing the data needed for this assignment
returnedData = requests.get(url) #Get the date from the URL
bitCoinDict = returnedData.json() #Store the data in this variable

for key, value in bitCoinDict['bpi'].items(): #Iterate through the items in the 'bpi section and displays each currency listed and their rates 
    print(key, ": ", end='') #Displays currency header
    print(value['rate']) #Displays the rate for the currency
    print() #Blank line to seperate the different currencies
