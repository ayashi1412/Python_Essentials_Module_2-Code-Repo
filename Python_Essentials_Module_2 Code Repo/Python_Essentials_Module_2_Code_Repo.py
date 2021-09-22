#Chapter 2 
#Written by: Binod Gurung

#Module 2.1.1.6 Print Function
print("Hello, Python!") #Displays Hello, Python!
print("Binod")          #Displays Binod.

#Module 2.1.1.18 Working with sep and end

print("Programming","Essentials","in", sep="***", end="...") #sep separates the arguments with *** and end ends the arugument with ...
print("Python")

#MODULE2.2.1.11 LAB Python Liberals

print('\"I\'m"\n\""learning""\n\"""Python"""')

#MODULE2.4.1.7 LAB Variables Adding values assisgned to variables.

John = 3
Mary = 5
Adam = 6
print(John , Mary , Adam, sep=",")
total_apples = John + Mary + Adam
print(total_apples)

#MODULE2.4.1.9 LAB Variables: A Simple Converter

kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#MODULE2.4.10 LAB: Operators and expressions

x =  0                                          #Assign value 0 to x.   
x = float(x)                                    #Conveting the value of x to float type and re-assign to x.
y = (3 * x ** 3) - (2 * x ** 2) + (3 * x) - 1   #Calculating the value of y from right binding.
print("y =", y)

#MODULE2.5.1.2 LAB: Comments - This program computes the number of seconds in a given number of hours

a = 2                                     # number of hours
seconds = 3600                            # number of seconds in 1 hour
print("Hours: ", a)                       #printing the number of hours
print("Seconds in Hours: ", a * seconds)  # printing the number of seconds in a given number of hours

#MODULE 2.6.1.9 LAB: Simple Input and Output. Evaluating the results of 4 arithmetic operations.
 
a = float(input("Enter the first float value: ")) # input a float value for variable a here
b = float(input("Enter the second float value: "))# input a float value for variable b here

print("The sum of the float values is: " + str(a + b))          # output the result of addition here
print("The difference of the float values is: " + str(a - b))   # output the result of subtraction here
print("The product of the float values is: " + str(a * b))      # output the result of multiplication here
print("The Quotient of the float values is: " + str(a / b))     # output the result of division here
print("\nThat's all, folks!")                                   #\n will start a newline after the print output.

#MODULE 2.6.1.10 LAB: Operators and expressions. Evaluate an algebric expression

x = float(input("Enter value for x: ")) #Input user's float value.
y = 1 / (x + (1/(x + (1/(x + (1/x)))))) # 1/x is represenation of 1/x in algrbric expression.
print("y =", y)

#MODULE 2.6.1.11 LAB: Operators and expressions. Evaluate the end time of a period of time.

hour = int(input("Starting time (hours): "))    #Input starting Time in hours.
mins = int(input("Starting time (minutes): "))  #Input starting Time in Minutes.
dura = int(input("Event duration (minutes): ")) #Input the event duration in Minutes.

Total_Minutes = (mins + dura)    #Calculates the total time spent in minutes.
End_Minutes = Total_Minutes % 60 #% 60 calculates the remainder of the minutes.
hr = hour + (Total_Minutes//60)  #//60 calculates the hour carried over.
End_hr = hr % 24                 #%24 calculates the 24 hr clock when the hr goes beyound 24.

print("The End time is ",End_hr,":",End_Minutes)

#End of Module
    