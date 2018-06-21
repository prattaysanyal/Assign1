//Q1. What is time tuple? // 
'''Time-tuple accepts an instant expressed in local time and
returns a string representing the instant as specified by string fmt.
Parses str according to format string fmt and returns the instant in
time-tuple format. Returns the current time instant, a floating-point
number of seconds since the epoch.'''

//Q2. WAP to get formatted time? //
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

//Q3. Extract month from the Time. //
import datetime
date = datetime.datetime.fromtimestamp(19800801)
print (date.month)

//Q4. Extract day from Time. //
import datetime
date = datetime.datetime.fromtimestamp(19800801)
print (date.day)

//Q5. Extract date from the Time. //
import datetime
d = datetime.now()
only_date = d.date()
only_date
datetime.date(2015, 11, 20)

//Q6. Program to print time using local time method. //
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

//Q7. Program to find the factorial of a number using math package functions. //
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

//Q9. Use OS Package to get current working directory. //
import os
print(os.getcwd())
