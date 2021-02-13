enterNum = int(input("Please enter a positive integer: ")) #User enters a number

#Function checks whether the user input is an odd or even number
def checkNum(enterNum):
    while enterNum > 1: #While the user input is greater than 1

        print(enterNum, end =' ') #Displays the users input and calculations from it until it gets to 1
        
        if enterNum % 2 == 0: #If the user input is a positive number 
                enterNum = enterNum // 2 #User input is divided by 2
        else: #If the user input is an odd number
                enterNum = (enterNum * 3) + 1 #User input is multiplied by 3 and adds one to the total

    print(1, end='') #Displays 1 as the end of the calculation or on its own if the user input is 1 in which case the while loop is ignored

checkNum(enterNum) #Runs the function