#A. Python is an indent based programming language
#Use Case 1:
#Add single-line and multi-line comments to describe what the below code does for Inceptez Technologies’ training tracker.
""""  This s the code for understanding Comments in Python
Here it describes the Students and Trainers available in Inceptez
"""

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


