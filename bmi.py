import math #Import the math module to be able to do calculations

#Program asks user for their height and then their weight

height = int(input("Enter your height (cm): ")) #User enters their height in centimeters
weight = int(input("Enter your weight (kg): ")) #User enters their weight in kilograms

temp = height/100 #Takes the user's height and divides it by 100

bmi = weight/(temp**2) #Takes the weight and divides that by the temp variable to the power of 2

#The program calculates the user's input and displays the user's BMI number
print("Your BMI is ", round(bmi, 2))  #BMI is rounded off to two decimal places

#Function used to display the user's weight range based on their BMI number
def weightRange():
    if bmi > 30: #If the BMI number is greater than 30
        print("You are in the Obese range") #User is classifed as Obese
    elif bmi >= 25 and bmi <= 29.9: #If the BMI number is greater or equal to 25 and is less or equal to 29.9
        print("You are in the Overweight range")#User is calassified as Overweight
    elif bmi >= 18.5 and bmi <= 24.9:#If the BMI number is greater or equal to 18.5 and is less or equal to 24.9
        print("You are in the Healthy range") #User is classified as Healthy
    elif bmi < 18.5: #If the BMI number is less than 18.5
        print("You are in the Underweight range")#User is classified as Underweight
    
weightRange() #Calls the above fucntion so that the program can run it