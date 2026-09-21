#A. Python is an indent based programming language
#Use Case 1:
#Add single-line and multi-line comments to describe what the below code does for Inceptez Technologies’ training tracker.
""""  This s the code for understanding Comments in Python
Here it describes the Students and Trainers available in Inceptez
"""
import string

#B. Commented line in Python

students = 100 # Total No.Of.Students
trainers = 2 #Trainers
total = students + trainers
print(total)

#Use Case 2:
#Convert the below block into a “dead code” using comments,
# then re-activate it later to print

#print("Welcome to Inceptez Python Learning")

# C.Playing With quotes
#Create three string variables that correctly store and print:

Str1= "This is Inceptez\'s \"Python\""
Str2="""This is Inceptez's "Python" Class for Data Engineers & AI Engineers"""
Str3= 'This is Inceptez\'s \"Python\"'
print(Str1)
print(Str2)
print(Str3)

#Multi Line Quotes

Str4= """
Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey. """
print(Str4)

#D. Let's learn all about VARIABLES
"""
Use Case 1:
Declare variables to store the following details: 
Student name,Course name,Institute Name
Then print a formatted message:
Name: Arun is learning the course Python Fundamentals at the institute Inceptez Technologies
"""
Student_Name="Nathiya"
Course_Name="Python Fundamentals"
Training_Institute_Name="Inceptez Technologies"
print(f"{Student_Name} is learning the course{Course_Name} @ the Institute {Training_Institute_Name}")
"""
Use Case 2:
Demonstrate dynamic inference, 
dynamic typing using with fee by applying .18 gst  and 
prove strongly typing character also by operating it 
with Eighteen percent gst

fee = 45000 """

fee= 45000
print(type(fee))
fee="18 Percent gst"
print(type(fee))
A=10
B="Hello"
#print(A+B) #Prove for Strongly Typing

#E. Variables Naming Conventions
#Use Case 1:
#Identify which variable names below are invalid for Inceptez’s student database:

# 2student = 'Ravi' -invalid  because, name should not starts with number
_student_id = 1001 #Valid
studentName = 'Priya' #Valid
#class name = 'Python' -Invalid because contains space
inceptez_batch = 'Morning'#Valid - Allowed Underscore for better readability
print(f"{studentName} with the id {_student_id} and batch belongs to {inceptez_batch} ")

#Use Case 2:
#Declare 3 variables following naming styles for Inceptez projects:



Batch= "DataEngineeringBatch" #Pascal
Batch2= "dataEngineeringBatch" #CamelCase
Batch3= "data_engineeringBatch" #Snake case

print(Batch)
print(Batch2)
print(Batch3)

#F. Type identification & Casting
"""
Use Case 1:
Write a program that asks for an employee’s age.
1. Checks its type is of string (think about using isinstance() function)
2. Converts it to int (continue writing your program from here..)
3. Prints the years pending for retirement, for eg. 60 is the retirement age.
Example:
Enter your age: 40
You will retire in 20 years at Inceptez Technologies.
"""
age=int(input("Enter your age"))
print(isinstance(age, int))
print(isinstance(age, str))

print(type(age))

if((60-age)>1 and (60-age)<=60):
    print(f"pending for retirement is  {60-age} years")
elif ( age>60) :
    print(f"your  retirement is Completed")
else :
    print(f"pending for retirement is  {60 - age} year")

"""Use Case 2 (Debug):
Fix the type error in the following code for salary calculation:

salary = '50000'
bonus = 10000
print('Total Salary in Inceptez:', salary + bonus) """

salary= 50000 #Remove the quotes
bonus= 10000
print('Total Salary in Inceptez:', salary + bonus)


#G. Data types and casting
'''Use Case 1 — Employee Salary Breakdown Using Numeric & String Types
Employee Salary Breakdown
a. Write a program that asks the user for:
employee_name (string)
base_salary (float)
hra_percent (integer)
bonus_amount (float) '''
employee_name =input("Enter an employee name: ")
salary = float(input("Enter your salary: "))
bonus = float(input("Enter your bonus: "))
hra_percent = int(input("Enter your hra_percent: "))

"""
B. Convert inputs to the correct datatype if required.
Calculate:
 HRA = base_salary * (hra_percent / 100)
 Total Salary = base_salary + HRA + bonus_amount """
HRA= salary * (hra_percent / 100)
Total_Salary= salary + HRA+bonus


# C. Print the output like this:
"""
Employee: Arun
Base Salary: 40000.0
HRA @ 20%: 8000.0
Bonus: 5000.0
Total Salary Payable: ₹53000.0"""
print("Employee",employee_name)
print("Base Salary",salary)
print("HRA @20%:",HRA)
print("Bonus",bonus)
print("Total Salary",Total_Salary)


"""
Use Case 2: Student Result Classification
a. Write a program that takes marks as input (initially as a string).
B. Check if the value can be converted to float.
C. Then classify (try using if condition with the help of AI, however we will learn about if condition soon):
Marks >= 90 --> Outstanding
 Marks >= 75 --> Excellent
 Marks >= 50 --> Pass
 Marks < 50 --> Fail
 
#D. If the input is not numeric, print:
 #Invalid marks entered — Please provide numeric input.
"""
print("Student Assessment")

Student_Name = input("Enter your name: ")
Total_marks = input("Enter total marks: ")

if not Total_marks.isnumeric():
    print("Enter Numeric value")
else:
    Total_marks = int(Total_marks)

    if Total_marks >= 90:
        print("Outstanding")
    elif Total_marks >= 75:
        print("Excellent")
    elif Total_marks >= 50:
        print("Pass")
    else:
        print("Fail")

print(f"The assessment of the student {Student_Name} ends here")
"""
Use Case 3: Bug Fixing — Datatype Mismatch
The below code is intended to calculate total price, but it has datatype errors. Fix it.
Incorrect code:
item_name = input("Enter product name: ")
 price = input("Enter price per item: ")
 quantity = input("Enter quantity: ")
total_cost = price * quantity
print("You purchased " + quantity + " units of " + item_name)
 print("Total payable: " + total_cost)
Expected output after fixing:
Enter product name: Notepad
 Enter price per item: 35.50
 Enter quantity: 3
You purchased 3 units of Notepad
 Total payable: 106.5 INR
"""

item_name = input("Enter product name: ")
price = float(input("Enter price per item: ")) #Corrected indentation , converts to float
quantity = int(input("Enter quantity: "))#Indendation  , convert to int
total_cost = price * quantity
print(f"You purchased " ,quantity , " units of " + item_name) # Str can be concatenate, added "," by removing +
print("Total payable: " , total_cost) #Replaced with ","


#H. Python Operators Usecases
"""
Use Case 1: Internet Data Usage Calculator
Write a program that asks the user for:
Total monthly data limit (in GB)
Data used so far (in GB)


Calculate using arithmetic operators:
 Remaining data = limit - used
 Usage percentage = (used / limit) * 100
Print:
Remaining data
Usage percentage rounded to 2 decimals


If usage percentage is greater than or equal to 80, print:
 "Warning: High usage, consider upgrading your plan."
"""
Total_Monthly_data_limit =float(input("Enter total monthly data limit(IN GB): "))
Data_Used_So_Far= float(input("Enter data used so far(In GB): "))
Remaining_data= Total_Monthly_data_limit - Data_Used_So_Far
Usage_Percentage=  (Data_Used_So_Far/Total_Monthly_data_limit)*100
print("Remaining Data",Remaining_data)
print("Usage Percentage",round(Usage_Percentage,2))

if Usage_Percentage >= 80:
    print("Warning: High usage, consider upgrading your plan.")
else :
    print("Enjoy ur browsing ")
"""
    Use Case 2: Shopping Discount Calculation
    Write a program that takes:
    Original price (float)
    Discount percent (int)

    Using assignment and arithmetic operators, calculate:
     Discount amount = (price * discount_percent) / 100
     Final price = price - discount_amount
    Print:
     Original price, discount applied, and final payable amount.
"""
Original_Price = float(input("Enter Original Price: "))
Discount_Percent = int(input("Enter Discount Percent: "))
Discount_Price = Original_Price * (Discount_Percent / 100)
Final_Price = Original_Price - Discount_Price

print("The Original Price", Original_Price)
print("The Discount_Price", Discount_Price)
print("The Final Price", Final_Price)

"""
Use Case 3 (Bug Fixing): Logical and Comparison Operator Errors
The following code should determine voting eligibility, but it contains operator mistakes. Fix it.
Incorrect code:
age = input("Enter age: ")
 citizen = input("Are you an Indian citizen? (yes/no)")
if age > "18" and citizen = "yes":
 print("Eligible to vote")
 else:
 print("Not eligible")
Expected behavior:
Convert age to integer before comparison.
Only print "Eligible to vote" if age is 18 or above AND 
citizen input is "yes" (case-insensitive). """
age = int(input("Enter age: "))
citizen = input("Are you an Indian citizen? (yes/no): ")
if age >= 18 and citizen.lower() == "yes": #Case INsensitive
 print("Eligible to vote")
else:
 print("Not eligible")
"""
I. Conditional Structure
Use Case 1: Banking Eligibility Check
Write a program that asks the user for:
Age
Monthly income


Conditions:
If age < 18: print "Not eligible for a bank account."
If age >= 18 and income < 15000: print "Eligible for basic savings account."
If age >= 18 and income between 15000 and 50000: print "Eligible for savings + salary account."
If age >= 18 and income > 50000: print "Eligible for premium account."
"""
Age = int(input("Enter age: "))
Monthly_income = int(input("Enter Monthly income: "))
if Age < 18:
    print("Not eligible for a bank account.")
elif  Age >= 18  and Monthly_income < 15000:
    print("Eligible for basic savings account.")
elif Age >= 18 and  Monthly_income >= 15000 and Monthly_income < 50000:
    print("Eligible for savings + salary account.")
elif Age >= 18 and Monthly_income > 50000:
    print("Eligible for premium account.")
"""
Use Case 2: Check room availability
-Check room availability
    - If available:
        - If guest is VIP
            → Offer complimentary upgrade
        - Else if member 5+ years
            → Offer discount
        - Else
            → Standard price
    - Else:
        → Show: "No rooms available" """


room = input("Check rooms available (Yes/No): ")

if room.lower() == "yes":
    guest = input("VIP (Yes/No): ")
    member = input("Member 5+ years (Yes/No): ")

    if guest.lower() == "yes" and member.lower() == "yes":
        print("Offer complimentary upgrade + discount")
    elif guest.lower() == "yes":
        print("Offer complimentary upgrade")
    elif member.lower() == "yes":
        print("Offer discount")
    else:
        print("Standard price")

"""
Use Case 3 (Bug Fixing): Nested Condition Logic Issue
Fix the following code so that it correctly determines whether the entered temperature indicates normal, fever, or high fever.
Incorrect code:
temp = input("Enter body temperature in Celsius: ")
if temp < "37":
 print("Normal temperature")
 elif temp > "37" and temp < "39":
 print("Fever")
 else
 print("High fever")
Expected behavior:
Convert temperature to float before comparison.


Conditions should print:
 Normal temperature (less than 37)
 Fever (between 37 and 39)
 High fever (39 and above)
"""


temp = float(input("Enter body temperature in Celsius: "))

if temp < 37:
 print("Normal temperature")
elif temp > 37 and temp < 39:
 print("Fever")
else :
 print("High fever")

#Scenario
"""
Select the most suitable transportation option based on available money 
and ticket prices.

Possible Options
Flight
Train
Bus
No transportation (because the budget is insufficient)
"""
Wallet =int(input("Enter the available money: "))

flight=6000
bus=3000
train=4200
if Wallet >= flight or Wallet >= bus or Wallet >= train :
    print("Eliglible for Travel")
    if  Wallet >= flight  or flight <=train and flight <=bus:
        print("You can travel by flight.The Fare is",flight)
    elif Wallet >=train or  train<=bus :
        print("You can travel by train.The fare is",train)
    elif Wallet >= bus :
        print("You can travel by bus.The fare is",bus)
else :
    print("No transporation ")