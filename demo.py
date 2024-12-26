'''
#----------Variables-------------
a=2
b=5
Length=10
Breadth=15
Area=200
Height=5
Volume=50
Age=50
Digit=12

#To know about the type of the variable
type(Area)
print(type(Area))

#-------------------Datatypes--

#--------------------Numbers

#integer
Int1=1234
Int2=-1234

#Longintergers
LongInt1=123456789101112131415161718192012345678910111213

#Floting point constants
pi = 3.14
print(pi)
print(type(pi))

Num_1=1234.5678
Num_2=10.5
Num3=12.34E3
Num4=10.0E2

#Complex Numbers

z = 3+4j
print(z)
print(type(z))

#2----Strings-----
digit = '5'
print(digit)
print(type(digit))

Str1="Hello World!"
print(Str1)
Name='John'

Alphabet_1='abcdefg'
Alphabet_2='hijklmnop'
Alphabet_3='qrstuvw'
Alphabet_4='xyz'

print(Alphabet_1+Alphabet_2+Alphabet_3+Alphabet_4)

English_Alphabets=Alphabet_1+Alphabet_2+Alphabet_3+Alphabet_4

len(English_Alphabets)#provides the number of characters


#Python supports multiline strings
aa = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""



#Convert an integer into string by str()builtin function
int1=123
int2str=str(int1)
print(int1)
print(int2str)

#Square brackets can be used to access elements of the string
string='I retuned a bag of groceries'
print(string)

#Indexing in python starts from '0' zero

print(string[0])
print(string[1])#it delivers a space


Str='HELLO PYTHON'
print(len(Str))

A=Str[0]

print(A)

print(Str[2])
print(Str[3])
print(Str[5])
print(Str[12])#index greater than upper bound will give an error


print(Str[len(Str)-1])#To fetch the last character in a string

#String Slicing
Str[0:5]
Str[:5]
Str[:]#gives the entire string
Str[::]#gives the entire string

#Str[:5]#substrings

Str[6:]

Str[8:10]

#Fetching the characters using negative indexing

print(Str[-1])#prints the last character
print(Str[-12])#prints the first character

print(Str[-12:-7])#Slicing using negative indexing

#String Concatenation
x = "All is "
y = "well"
z =  x + y
print(z)

x = "All is"
y = "well"
z =  x + y
print(z)

s1 = 'hello'
s2 = 'world'

s3 = s1 + ' ' + s2#add a space 
print(s3)

#some other operations

s = 'hello how are you ?'

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.split(' '))

#Operators in python--
a = 7
b = 3

sum =  a+b
print(sum)

diff =  a-b
print(diff)

pro =  a*b
print(pro)

ratio =  a/b
print(ratio)

rem =  a%b
print(rem)

quo =  a//b
print(quo)

#Console Input (function used to read data from user)

name = input("Enter your name : ")

print("Your name is",name)

age = int(input("Enter your age : "))
#age = int(age)
print(age)
print(type(age))

weight = float(input("Enter your weight : "))
print(weight)
print(type(weight))


#---------------------------1--------------
#Program to find the sum and average of three numbers

num1 = int(input('Enter number 1 : '))
num2 = int(input('Enter number 2 : '))
num3 = int(input('Enter number 3 : '))

sum = num1 + num2 + num3
avg = sum/3

print("Sum = ",sum)
print("Average = ",avg)

#----------------------------2--------------------------

#Program to find the length of the hypotenuse of a triangle if the other two sides are given

sideA=3
sideB=4
sideC=(sideA**2+sideB**2)**0.5
print('The lingth of sideC is',sideC)

#with lengths are directly entering from the console

sideA=int(input('Enter the length of sideA:'))
sideB=int(input('Enter the length of sideB:'))

sideC=(sideA**2+sideB**2)**0.5
print('The length of sideC is',sideC)

#----------------------------------------------3-----------------------
#creating a newword from an existing word

Name='Sophus Lie'
print(Name)
NewWord=Name[3]+Name[1]+Name[4]+Name[5]+Name[9]
print(NewWord)

#------------------EURO to INR Converter----
#Prompt for the Exchange rate
Exchange_Rate = float(input("Enter the exchange rate (1 EUR to INR): "))
    
# Prompt for the amount in Euros
Euro_amount = float(input("Enter the amount in Euros: "))
    
    # Calculate the amount in Indian Rupees
INR_amount = Euro_amount * Exchange_Rate
    
# Display the result
print('The amount in INR:',INR_amount)
'''
import pandas as pd
data=pd.series([0.25,0.5,0.75,1.0])
print(data)
