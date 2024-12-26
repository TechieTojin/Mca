'''
#1. Write a program to print the sum and average of 3 numbers,
#by entering the numbers directly from the console.

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate sum and average
total_sum = num1 + num2 + num3
average = total_sum / 3

# Print the results
print("Sum of the numbers:", total_sum)
print("Average of the numbers:", average)

#2. Write a short program that computes the length of the hy-
#potenuse of a right triangle given the two legs. The program may use three variables, sideA, sideB, and sideC.

# Get input from the user
sideA = float(input("Enter the length of the first leg of the triangle: "))
sideB = float(input("Enter the length of the second leg of the triangle: "))

# Calculate the length of the hypotenuse
sideC = (sideA**2 + sideB**2)**0.5

# Print the result
print("The length of the hypotenuse is:", sideC)

#3. Sophus Lie was a Norwegian mathematician. Write a program to print the name Sophus Lie. Then, without writing the string literal “house”, modify it to print the string“house”, from the name, Sophus Lie to the screen using string indexing
# Print the name
name = "Sophus Lie"
print("Name:", name)

# Extract "house" from "Sophus Lie" using string indexing
# The word "house" is hidden in the name "Sophus Lie" in a specific manner:
# 'house' can be extracted by finding appropriate indices
# Let's print "house" by slicing and concatenating characters

# Finding and printing "house"
house = name[1:6] + name[7:8] + name[9:10] + name[10:11] + name[12:13]
print("Extracted string:", house)

'''
#4. Write a program that converts the Euro to a INR. You can do this by finding the exchange rate on the internet and then prompting for the exchange rate in your program.
 # Prompt the user for the exchange rate
exchange_rate = float(input("Enter the exchange rate from Euro to INR: "))

# Prompt the user for the amount in Euros
euros = float(input("Enter the amount in Euros: "))

# Convert Euros to INR
inr = euros * exchange_rate

# Print the result
print(f"{euros} Euros is equal to {inr} INR.")
