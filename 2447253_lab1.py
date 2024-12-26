# 2447253 TOJIN VARKEY SIMSON LAB-1 EXERCISE

# 1)Declare a python datatype list and do the following:
#(a) Write a Python program to sum all the items of the list.
#(b) Write a Python program to multiply all the items.
#(c) Write a Python program to get the largest number from a list.
#(d) Write a Python program to get the smallest number from a list.

l1=[14,63,8,34,89,120,44]
#a)
sum=0
for i in l1:
    sum=sum+i
print("sum all the items of the list:",sum)

#b)
prod=1
for i in l1:
    prod*=i
print("Product all the items:",prod)

#c)
l=l1[0]
for i in l1:
  if (i>l):
     l=i
print("the largest number from the list is: ",l)

#d)
s=l1[0]
for i in l1:
  if (i<s):
     s=i
print("the largest number from the list is: ",s)

# 2) Let A=[‘abc’, ‘xyz’, ‘aba’, 1221’] be a given string, and write a Python
#program that prints the string or strings and their index from the given list,
#ensuring that the first and last characters of the strings to be printed are
#identical.

A=['abc', 'xyz', 'aba', '1221']
print("the first and last characters of the strings that are identical:")
for i in A:
    n=len(i)
    if i[0]==i[n-1]:
        print(i)

#(3) Write a python program to print patterns given below:

# Define the number of rows for the letter pattern
rows = 5

# Print the letter pattern
for i in range(rows):
    # Print leading spaces
    print(' ' * (rows - i - 1), end=' ')
    # Print characters
    for j in range(i + 1):
        print(chr(65 + j), end=' ')
    # Move to the next line
    print()

print("\n")  # Newline for separating patterns

# Print the star pattern
for i in range(1, rows):
    for j in range(i):
        print("* ", end='')
    print(" ")

# 4)Write a Python program to convert the given list to a list of dictionaries.
#ListColour= ["Black", "Red", "Maroon", "Yellow"], ["000000", "FF0000",
#"800000", "FFFF00"]
#Expected Output: {’colorName’: ’Black’, ’colorCode’: ’000000’}, {’color-
#Name’: ’Red’, ’colorCode’: ’FF0000’}, ’colorName’: ’Maroon’, ’colorCode’:
#’800000’}, {’colorName’: ’Yellow’, ’colorCode’: ’FFFF00’}

color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["000000", "FF0000", "800000", "FFFF00"]

# Initialize an empty list to hold the dictionaries
color_list = []

# Use a for loop with an index to iterate through the lists
for i in range(len(color_names)):
    color_dict = {'colorName': color_names[i], 'colorCode': color_codes[i]}
    color_list.append(color_dict)

# Print the result
for color in color_list:
    print(color)

#(5) Write a Python program to print all the even numbers and their squares
#within the given range.
#(a) range(1,50)
#(b) range(1,100)


#a)
print("all the even numbers and their squares")
for i in range(1,50):
    if (i%2==0 and i**2<50):
        print ("even no.= ",i," and its square=",i**2)

#b)
print("\n")        
for i in range(1,100):
    if (i%2==0 and i**2<100):
        print ("even no.= ",i," and its square=",i**2)

#(6) Write a Python program to read a four-digit number and find its
#(a) Sum of digits
#(b) Reverse


n=int(input("enter a four-digit number:"))
sum1=0
rev=0
while(n!=0):
    rem=n%10
    sum1=sum1+rem
    rev=(rev*10)+rem
    n=n//10

print("Sum of digits= ",sum1)
print("Reverse of digits= ",rev)

#(7) Write a program to find the area of a triangle. Then find the area of two
#arbitrary triangles by entering the three sides both using the input function
#(input()). Print the total area enclosed by both triangles and each triangle’s
#contribution (%) towards it.
#Hint: area of a triangle:
#A =s(s − a)(s − b)(s − c) s =
#       a + b + c
#            2


import math

def calculate_area(a, b, c):
    # Calculate semi-perimeter
    s = (a + b + c) / 2
    # Calculate area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Input the sides for the first triangle
a1 = float(input("Enter the first side of the first triangle: "))
b1 = float(input("Enter the second side of the first triangle: "))
c1 = float(input("Enter the third side of the first triangle: "))

# Input the sides for the second triangle
a2 = float(input("Enter the first side of the second triangle: "))
b2 = float(input("Enter the second side of the second triangle: "))
c2 = float(input("Enter the third side of the second triangle: "))

# Calculate areas
area1 = calculate_area(a1, b1, c1)
area2 = calculate_area(a2, b2, c2)

# Calculate total area
total_area = area1 + area2

# Calculate percentage contributions
percentage1 = (area1 / total_area) * 100
percentage2 = (area2 / total_area) * 100

# Print results
print(f"Area of the first triangle: {area1:.2f}")
print(f"Area of the second triangle: {area2:.2f}")
print(f"Total area enclosed by both triangles: {total_area:.2f}")
print(f"Contribution of the first triangle: {percentage1:.2f}%")
print(f"Contribution of the second triangle: {percentage2:.2f}%")

#(8) Given a dictionary containing the following information about 10 different
#people:
#Write a Python program that prints each person’s name, age, and blood
#group in a formatted manner. Each person’s information should be separated
#by a line of dashes (-).(Dictionary given in this problem can be found from the attached notepad )
#Expected output:

people = [
    {"name": "John Doe", "age": 30, "blood_group": "A+"},
    {"name": "Jane Smith", "age": 25, "blood_group": "B-"},
    {"name": "Emily Davis", "age": 40, "blood_group": "O+"},
    {"name": "Michael Brown", "age": 35, "blood_group": "AB-"},
    {"name": "William Johnson", "age": 28, "blood_group": "A-"},
    {"name": "Emma Wilson", "age": 22, "blood_group": "B+"},
    {"name": "Oliver Martinez", "age": 33, "blood_group": "O-"},
    {"name": "Sophia Anderson", "age": 27, "blood_group": "AB+"},
    {"name": "James Thomas", "age": 45, "blood_group": "A+"},
    {"name": "Isabella Lee", "age": 38, "blood_group": "B-"}
]
for i in people:
    print("Name :",i['name'])
    print("Age :",i['age'])
    print("Blood Group :",i['blood_group'])
    print("-------------------")


#9)Write a Python program to extract the rear elements from a tuple string as
#depicted in the following figure:

print("\n")
t=("python","learn","includehelp")
li=[]
for i in t:
    n=len(i)
    li.append(i[n-1])
print(li)

#10)Declare a list/tuple containing all the twelve months. Write a Python program
#that converts a month name entered via the Python console to the number
#of days in that month (Consider leap year as well the code):
#Expected Output:
print("\n")
months=['january','february','march','april','may','june','july','august','september','october','november','december']
e=input("enter the month name: ")
if(e==months[0] or e==months[2] or e==months[4] or e==months[6] or e==months[7] or e==months[9] or e==months[11]):
    print("no.of days in ",e,"is 31.")
elif(e=="february"):
    year=int(input("enter the year: "))
    
    if (year % 400 == 0) and (year % 100 == 0):
        print("no.of days in ",e,"is 29.")
    elif (year % 4 ==0) and (year % 100 != 0):
        print("no.of days in ",e,"is 29.")
    else:
        print("no.of days in ",e,"is 28.")
else:
    print("no.of days in ",e,"is 30.")




