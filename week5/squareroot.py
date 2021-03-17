#Calculates the square root of a given number using the Newton method
def calcSquareRoot(givenNum):
    x = givenNum #Assign givenNumber to a new variable

    while True: 
        calRoot = 0.5 * (x + (givenNum / x))  #Calculates an initial square root

        if (abs(calRoot - x) < 0.1): #If the calculated root comes inside of the tolerence then the loop ends
            break 

        x = calRoot #Assign new root to x and loop again until the above code happens

    return calRoot

#Gets the root and displays it through print statements as well as error checking for
#anything that isn't positive number
def getSquareRoot():
    
    while True:
        try:
            enterNum = float(input("Please enter a positive number: ")) #User enters number
            sqrt = calcSquareRoot(enterNum)#Call previous method and assign the entered number as the argument for that method
            print("The square root of " + str(enterNum) + " is approx. " + "{:.1f}".format(sqrt)) #Formats given root to a single decimal place
        except ValueError: #If the user enters letters or characters
            print("You must enter a positive number - no characters allowed")
        except ZeroDivisionError: #If the user enters 0
            print("You must enter a positive number - no zeros allowed")

getSquareRoot()
