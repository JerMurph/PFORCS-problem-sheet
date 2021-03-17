import math #Import the math module to be able to do calculations

#Program asks user for their height and then their weight

#Defined variables with default values so that the functions can access them
height = 0 
weight = 0
bmi = 0

#Function used to display the user's weight range based on their BMI number
#https://patient.info/doctor/bmi-calculator-calculator used as a reference for the the weight ranges
def weightRange():
    if bmi > 30: #If the BMI number is greater than 30
        print("You are in the Obese range") #User is classifed as Obese
    elif bmi >= 25 and bmi <= 29.9: #If the BMI number is greater or equal to 25 and is less or equal to 29.9
        print("You are in the Overweight range")#User is calassified as Overweight
    elif bmi >= 18.5 and bmi <= 24.9: #If the BMI number is greater or equal to 18.5 and is less or equal to 24.9
        print("You are in the Healthy range") #User is classified as Healthy
    elif bmi < 18.5: #If the BMI number is less than 18.5
        print("You are in the Underweight range")#User is classified as Underweight

def enterCalculateBMI():
    #Program will keep asking to enter your weight and height until a valid response is accepted
    #Anything but a number is entered and the program throws an error message and starts asking for input again
    while True: 
        try:
            height = int(input("Enter your height (cm): ")) #User enters their height in centimeters
            weight = int(input("Enter your weight (kg): ")) #User enters their weight in kilograms
        except ValueError:
            print("Enter a number") #Error stating a number must be entered
        else:
            temp = height/100 #Takes the user's height and divides it by 100
            bmi = weight/(temp**2) #Takes the weight and divides that by the temp variable to the power of 2

            #Calculates the user's input and displays the user's BMI number
            print("Your BMI is ", round(bmi, 2))  #BMI is rounded off to two decimal places

            weightRange() #Calls the weightRange function so that the program can run it

            break #Breaks out of the while loop and ends the program

enterCalculateBMI() #Calls the enterCalculateBMI function to run it and start the program
