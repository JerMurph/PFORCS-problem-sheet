# PFORCS-problem-sheet

All the weekly tasks for the GMIT module Programming for Cybersecurity.

Created by Jerry Murphy.

All the code in this repository was done on Microsoft Visual Studio.

<h2><b>Weekly Task #2: bmi.py</b></h2>

<b>Task:</b></br>
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

<b>Task:</b></br>
<i>Write a program (bitcoin.py) that prints out todays bitcoin price in dollars.</i>

<b>Solution:</b></br>
Running the program will make a request to the given URL and gathers the data from it, more specifically the data attaining to the current Bitcoin rate in Euros, British Pounds and US Dollars. The program uses a for loop to iterate through the section labelled 'bpi' which contains the necessary data required for the program and displays the current rate for each curreny.

<b>References:</b></br>
<a href="https://api.coindesk.com/v1/bpi/currentprice.json">Bitcoin Current Price</a> - URL containing the JSON data used in the program which contains the currency rates.</br>
<a href="jsonlint.com">JSONLint</a> - Used to tidy up the JSON data from the URL as it was difficult to read it.

<h2><b>Weekly Task #4: collatz.py</b></h2>

<b>Task:</b></br>
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

<h2><b>Weekly Task #6: es.py</b></h2>

<b>Task:</b></br>
Write a program that reads in a text file and outputs the number of e's it contains.</br>

The program should take the filename from an argument on the command line.</br>

$ python es.py moby-dick.txt</br>
116960</br>

<b>Solution:</b></br>
The program, through a command line for which I used the cmder command line and put the es.py and moby-dick.txt into the directory in order to make it work, opens up using the command "python es.py moby-dick.txt" and reads and the program then iterates through the entire file and when it encounters an e, it increase the count by one and does this until it gets to the end of the file.

<b>References:</b></br>
<a href="https://www.gutenberg.org/files/2701/old/moby10b.txt">The Project Gutenberg Etext of Moby Dick</a> - Source of the filename used for the program

<h2><b>Weekly Task #7: extract-url.py</b></h2>

<b>Task:</b></br>
Write a program called extract-url.py, that will extract the URLs from an access.log file. </br>

ie The part of the URL that is stored in the access.log file, complete with the query parameters (I am aware that the host name is not stored in this file, the referring host is)</br>

The program should store the URLs as strings in a list</br>

[</br>
'/cart.do?action=view&itemId=EST-6&productId=SC-MG-G10&JSESSIONID=SD5SL9FF2ADFF4958',</br>
'/category.screen?categoryId=SHOOTER&JSESSIONID=SD7SL9FF5ADFF5066' </br>
]</br>

Store the URLs as a Dictionary object in the list with the resource and parameter names and values separated out eg</br>

[</br>
   {</br>
     'resource':'cart.do', </br>
     'parameters':{</br>
         'action':'view',</br>
         'itemId':'EST-6',</br>
         'productId':'SC-MG-G10'</br>
         'JSESSIONID':'SD5SL9FF2ADFF4958'</br>
     }</br>
   },</br>
   #next dictionary object</br>
]</br>

<b>Solution:</b></br>
The program reads from the access.log file and reads through the file and grabs all the urls and extracts the query parameters while ignoring the host name and stores them in a list. Next, the program then splits up the url parameters and splits them up and sorts them into two categories: resource and parameters which are then added to a dictionary. Resources are split from the '/' tp the '?' and the parameters by the '&'.

<h2><b>Weekly Task #8: plottask.py</b></h2>

<b>Task:</b></br>
Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.</br>
Some marks will be given for making the plot look nice.</br>

<b>Solution:</b></br>
I intialize the X-Axis with the given range and then the Y-Axes with the given functions. Next I add colors and labels for each of the Y-Axes to keep it neat and organized and make the graph easier to read and also labels to display where the X and Y-Axes are. Finally I add a legend so that everything I mentioned previously can be displayed on the graph.

<b>References:</b></br>
<a href="https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html">Matplotlib: Plot a Function y=f(x)</a> - Used to figure out how to add colors and labels to the Y-Axes to make the graph much neater</br>

<h2><b>Weekly Task #9: weeklyTask9.py</b></h2>

<b>Task:</b></br>
I want to find which sessionId downloaded the most data</br>
Read the access.log into a dataframe (see lab)</br>
Set the date time to be the index (you will need to manipulate this data, see lab)</br>
Use regular expressions to extract the session id from the URLs and store them in a different column (use the apply function, see lab)</br>
Use groupBy to get the sum of all the data downloaded by each sessionId.</br>
Create a plot of this (type of your choice)</br>
Work out the amount of data each sessionId downloaded in any given day</br>

<b>Solution:</b></br>
