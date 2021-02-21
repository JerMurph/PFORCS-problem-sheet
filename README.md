# PFORCS-problem-sheet

All the weekly tasks for the GMIT module Programming for Cybersecurity.

Created by Jerry Murphy.

All the code in this repository was done on Microsoft Visual Studio.

<h2><b>Weekly Task #2: bmi.py</b></h2>

<b>Task:</b>

<i>Write a program that calculates somebody's Body Mass Index (BMI).</br>
The inputs are the person's height in centimetres and weight in kilograms.</br>
The output is their weight divided by their height in metres squared.</br>

$ python bmi.py</br>
Enter weight: 65</br>
Enter height: 180</br>
BMI is 20.06.</br></i>

<b>Solution:</b></br>
Running the programing will ask the user to enter their height in centimetres. Next, it will ask the user to enter their weight in kilograms. The program then calculates the BMI number from the user's input and displays a message to give the user their BMI number and also their weight range. I used a BMI calculator that I found through Google as a reference when making the program so that I was certain the calculations where correct and that I was getting the same BMI number in my program as the website's BMI calculator. I also used it to add an extra feature to my program to give the user their weight range based on what their BMI number is so for example, if the user was given a BMI number of less than 18.5 then the user is classified as Underweight, if it's greater than 18.5 but less than 24.9 then the user is classified as Healty, if it's greater than 24.9 but less than 29.9 then the user is classified as Overweight and if it is greater than 29.9 than the user is classified as Overweight. While it may not have been necessary to include weight ranges for this task, I thought I should add it in as an extra feature. The program also forces the user to only enter numbers when asked for input, anything else will throw a message asking the user to enter a number and start again.

<b>References:</b></br>
<a href="https://patient.info/doctor/bmi-calculator-calculator">BMI Calculator</a> - Used as a reference when making the program.

<h2><b>Weekly Task #3: bitcoin.py</b></h2>

<b>Task:</b>
<i>Write a program (bitcoin.py) that prints out todays bitcoin price in dollars.</i>

<b>Solution:</b></br>
Running the program will make a request to the given URL and gathers the data from it, more specifically the data attaining to the current Bitcoin rate in Euros, British Pounds and US Dollars. The program uses a for loop to iterate through the section labelled 'bpi' which contains the necessary data required for the program and displays the current rate for each curreny.

<b>References:</b></br>
<a href="https://api.coindesk.com/v1/bpi/currentprice.json">Bitcoin Current Price</a> - URL containing the JSON data used in the program which contains the currency rates.</br>
<a href="jsonlint.com">JSONLint</a> - Used to tidy up the JSON data from the URL as it was difficult to read it.

<h2><b>Weekly Task #4: collatz.py</b></h2>

<b>Task:</b>
<i>Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.</br>
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.</br>
Have the program end if the current value is one.</br>

$ python collatz.py</br>

Please enter a positive integer: 10</br>

10 5 16 8 4 2 1</i></br>

<b>Solution:</b></br>
The program asks the user to enter a positive number. The number entered by the user is calculated based on whether it is an odd or even number and continues until the current value is one by which point both program ends. If the number is even, the number is then divided by 2. If the number is odd, it is multiplied by 3 and has a 1 added to the end of it. If the user enters 1 then the program automatically ends. The program displays the initial user input and the current number from each calculation until the current value is 1.

<h2><b>Weekly Task #5: squareroot.py</b></h2>

<b>Task:</b></br>
<i>Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x)

I suggest that you look at the newton method at estimating square roots

$ python squareroot.py</br>
Please enter a positive number: 14.5</br>
The square root of 14.5 is approx. 3.8.</i></br>

<b>Solution:</b></br>
The program asks the user to enter a positive number. When entered, the program then assigns the input as an argument to the first method (calcSquareRoot) and assigns it to a new variable. The root is then calculated using a while loop which keeps iterating until the calculated root comes inside the tolerence and breaks out of the loop and activates displays the square root to the nearest decimal point.

<b>References:</b></br>
<a href="https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/">Find root of a number using Newton’s method</a> - Used as a reference for figuring out how to do the Newton method
