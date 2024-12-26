#python tutoral 2

#1
'''
Write a Python program that executes an operation on a list and handles an
‘IndexError’ exception if the index is out of range.
'''
l1=[2,4,6,12,43]
try:
      m=l1[6]
      print(m)
    
except IndexError:
      print("Error:Out of index error.")
finally:
      print("Finished")

#2
'''
Write a program that divides two numbers provided by the user. The program should handle the following exceptions::
(a) a ‘ValueError; if the user does not enter a number.
(b) ‘ZeroDivisionError’ if the user attempts to divide by zero.
(c) An unexpected exception using a generic Exception handler.
'''
try:      
  a=int(input("enter 1st no.:")) 
  b=int(input("enter 2st no.:"))
  c=a/b
  print(hi)
except ValueError:
  print("value not given")
except ZeroDivisionError:
  print("trying to divide by zero so error.")
except Exception as e:
  print("unexpected exception as ",e)

#3
'''
Write a function get_integer_input(prompt) that prompts the user to enter
an integer. If the user enters anything other than an integer (e.g., a string like
‘five’), the function should catch the ValueError and prompt the user again
until a valid integer is entered. The function should return a valid integer.
'''
def get_integer_input(prompt):
      while(1):
            try:
               user=input(prompt)
               p=int(user)
               print("you have entered an integer ",p)
               break
            except ValueError:
               print("Error: ",user," is not a vaild integer.enter a number.")
        
get_integer_input("Please enter an integer: ")

#4
'''
Write a function validate_user_input(str) that takes a string as input and checks the following:
(a) The string must be at least 8 characters long.
(b) The string must contain at least one digit.
(c) The string must contain at least one uppercase letter.
If any of these conditions are not met, the function should raise a custom exception InvalidInputError with a message specifying which condition failed.
'''
class InvalidInputError(Exception):
      pass
def validate_user_input(s):
      if len(s) < 8:
            raise InvalidInputError("String must be at least 8 characters long.")
          
      if not any(char.isdigit() for char in s):
            raise InvalidInputError("The string must contain at least one digit.")
    
      if not any(char.isupper() for char in s):
           raise InvalidInputError("The string must contain at least one uppercase letter.")
try:
      s="FamilyLove 2"
      validate_user_input(s)
      print(s,"Is a valid string.")
except InvalidInputError as e:
      print(e)

#5
'''
Write a Python program for an interactive calculator that:
(a) Continuously prompts the user to enter a simple arithmetic formula consisting of a number, an operator (+ or -), and 
another number, all separated by spaces (e.g., "3 + 5").
(b) Splits the user input using str.split() and checks if the input is valid. The input is valid if:
(i) It consists of exactly three elements.
(ii) The first and third elements can be converted to floating-point numbers.
(iii) The second element is either ’+’ or ’-’.
(c) If the input is invalid, the program should raise a FormulaError, a custom exception, with an appropriate error message.
(d) If the input is valid, the program should perform the calculation and print the result.
(e) The program should keep running until the user types "quit".
'''
class FormulaError(Exception):
      pass
while(1):
     p=input("enter a simple arithmetic formula consisting of a number, an operator (+ or -), and another number, all separated by spaces: ")
     l=p.split(" ")
     print(l)
     try:
          if len(l)!=3:
               raise FormulaError("The input should consist of exactly three elements")
          try:
            n1=float(l[0])
            n2=float(l[2])
          except ValueError:
            raise FormulaError("The first and third elements should be able to converte to floating-point numbers. ")
          if (l[1] != '+') and (l[1] != '-') :
               raise FormulaError("The second element should either '+' or '-'.")
          else:
               if l[1]=='+':
                 print("Result = ",n1 + n2)
               else:
                  print("Result = ",n1 - n2)  
               u=input("Enter quit to exit or just press enter:")
               if u=="quit":
                    break
     except FormulaError as e:
          print(e)


#6 Write a Python program that matches a string that has the letter ‘a’ followed by zero or more b’s.
import re
s1="abuzment"
pattern="ab*"
result= re.findall(pattern,s1)
print(result)

#7 Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
s2="Abuzment"
pattern="[A-Z][a-z]"
result1= re.findall(pattern,s2)
print(result1)

#8 Write a Python program that matches a word at the beginning of a string
import re
txt = "The rain in Spain"
result2= re.search(r'\w',txt)
print(result2)

#9
'''
Write a function validate_email(email) that checks if a given email address
is valid using regular expressions. A valid email should follow this format:
(a) It should start with one or more alphanumeric characters or underscores.
(b) It should contain exactly one ’@’ symbol.
(c) It should then contain one or more alphanumeric characters.
(d) It should end with a valid domain name (e.g., .com, .org, .edu).
If the email is not valid, raise a custom InvalidEmailError exception with an appropriate error message.
'''
import re
class InvalidEmailError(Exception):
     pass

def validate_email(email):
     pattern1=r'(^\w+)'
     m1=re.search(pattern1,email)
     pattern2=r'(@{1})'
     m2=re.search(pattern2,email)
     pattern3=r'(@\w+)'
     m3=re.search(pattern3,email)
     pattern4='(.com|.org|.edu)$' #or '(.com|.org|.edu)\Z'
     m4=re.search(pattern4,email)
     try:
          if m1==None:
              raise  InvalidEmailError("ERROR: valid email should start with one or more alphanumeric characters or underscores. ")
          if m2==None:
               raise  InvalidEmailError("ERROR:valid email should contain exactly one '@' symbol.")
          if m3==None:
              raise  InvalidEmailError("ERROR:valid email should then contain one or more alphanumeric characters.")
          if m4==None:
               raise  InvalidEmailError("ERROR:valid email should end with a valid domain name (e.g., .com, .org, .edu).")
          print("You have entered a vaild email.")
               
     except InvalidEmailError as e:
          print(e)

email='jai12@gmail.com'
validate_email(email)

#10
'''
Write a function that checks if a password is strong using regular expressions.
A strong password should:
(a) Be at least 8 characters long.
(b) Contain both uppercase and lowercase letters.
(c) Include at least one digit.
(d) Have at least one special character (e.g., @, #, $).
If the password is not strong enough, raise a custom ‘WeakPasswordError’ exception with a message indicating which criteria were not met.
'''
import re
class WeakPasswordError(Exception):
     pass
def passStrength(password):
     p1='.{8,}'
     m1=re.search(p1,password)
     p2='(?=.*[a-z])(?=.*[A-Z])' # ?= is a positive lookahead assertion.it ensures that the specified pattern exists but doesn’t actually include it in the overall match.
     m2=re.search(p2,password)
     p3=r'\d+'
     m3=re.search(p3,password)
     p4='[!@#$%^&*(),.?":{}|<>]'
     m4=re.search(p4,password)
     try:
          if m1==None:
              raise  WeakPasswordError("ERROR: strong password should be at least 8 characters long.")
          if m2==None:
               raise  WeakPasswordError("ERROR: strong password should Contain both uppercase and lowercase letters.")
          if m3==None:
              raise  WeakPasswordError("ERROR: strong password Include at least one digit.")
          if m4==None:
               raise  WeakPasswordError("ERROR: strong password Have at least one special character (e.g., @, #, $).")
          print("You have entered a vaild password.")
               
     except WeakPasswordError as e:
          print(e)

password='3455AA$JAq'
passStrength(password)


#11 Write a NumPy program to test whether none of the elements of a given array are zero.
import numpy as np
a1=np.array([[[1, 2], [3, 0]], [[5, 6], [7, 8]]])
c=0
for x in np.nditer(a1): #np.nditer() is a short command to itereate through all the iterations without 3 for loops
    if x==0:
        c=1
        break
if c==1:
    print("Elements of the array contain 0.")
else:
    print(" None of the elements of a given array are zero.")

#12 Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
import numpy as np
#2D array creations using zeros and ones

a2=np.zeros(([10,10]),dtype=int)
a2[0,:]=1 #making the 1st row elements as 1
a2[-1,:]=1
a2[:,0]=1
a2[:,-1]=1
print("Matrix, in which the elements on the borders will be equal to 1, and inside 0:")
print(a2)

#13 Write a NumPy program to calculate the absolute value element-wise.
import numpy as np
a3=np.array([[[-1, -2], [-3, 0]], [[-5, 6], [7, -8]]])
print("original array:\n",a3)
absolute_array=np.abs(a3)
print("Element vise absolute value:")
print(absolute_array)

#14 Write a NumPy program to compute the inner product of two given vectors.
import numpy as np
vector1 = np.array([3, 2, 1])
vector2 = np.array([4, 5, 6])
# Find the inner product using numpy.dot
inner_product = np.multiply(vector1, vector2) #ie (3x4)+(2x5)+(1x6)
print("The inner product of two given vectors:\n",inner_product) 
          
#15 Write a NumPy program to find the inverse of a given matrix.
import numpy as np
a4=np.array([[1, 2], [7, 8]])
if np.linalg.det(a4) == 0:
    print("The matrix is singular and does not have an inverse.")
else:
    inverse_mat = np.linalg.inv(a4)
    print("The inverse of a given matrix:\n",inverse_mat)

#16 Write a NumPy program to find the determinant of a given matrix
import numpy as np 
a5=np.array([[2,6,2],[6,5,4],[3,1,2]])
m=a5.shape[0]#no of rows
n=a5.shape[1]#no of columns
if m==n:
     deter=np.linalg.det(a5)
     print("Determinant of a given matrix:\n",deter) 
else:
     print("Can not find determinant of a non-square matrix.")
     
#17 Write a NumPy program to multiply any two arbitrary matrices.
import numpy as np

# Define the first matrix (2x3)
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

# Define the second matrix (3x2)
matrix2 = np.array([[7, 8],
                    [9, 10],
                    [11, 12]])

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

m=matrix1.shape[1] #for no.of columns
n=matrix2.shape[0] #for no.of rows
if m==n:
     # Multiply the matrices using np.dot()
     result = np.dot(matrix1, matrix2) #or result = matrix1 @ matrix2
     print("\nResult of matrix multiplication:")
     print(result)
else:
     print("Matrix multiplication not possible as no.of columns of 1st marix not equal to no.of rows of 2nd matrix.")

#18 Write a NumPy program to get the powers of an array values element-wise.
import numpy as np
base_array = np.array([1, 2, 3, 4, 5])
exponent_array = np.array([2, 3, 2, 1, 0])
result = np.power(base_array, exponent_array)

print("Base array:", base_array)
print("Exponent array:", exponent_array)
print("Result of element-wise exponentiation:", result)

#19
'''
(a) Compute the following statistics:
(i) Total population for each year.
(ii) Average population for each year.
(iii) Standard deviation of population for each year.
(iv) Country with the maximum population growth over the years.
(b) Raise a custom ‘DataConsistencyError’ if all data for a year or country
is missing.
(c) Ensure the input array is a 2D NumPy array.
(d) raise a InvalidDataError if input validation fails.
'''
import numpy as np
class DataConsistencyError(Exception):
    pass
class InvalidDataError(Exception):
    pass

popdata=np.array([[97.0,175.35,128.7,175.95,70.8],
                  [71.0,90.3,150.7,138.0,165.6],
                  [190.0,113.4,97.9,157.55,165.6],
                  [131.0,78.75,139.7,140.3,70.8],
                  [198.0,173.25,141.9,151.8,178.8],
                  [79.0,206.85,216.7,220.8,98.4],
                  [59.0,185.85,90.2,93.15,196.8],
                  [78.0,88.2,195.8,204.7,123.6],
                  [183.0,92.4,73.7,148.35,218.4],
                  [155.0,96.6,89.1,195.5,61.2]])
try:
    if popdata.ndim != 2:
        raise InvalidDataError("Input data must be a 2D NumPy array.")

        # Check for missing data
    if np.all(np.isnan(popdata), axis=0).any():
        raise DataConsistencyError("All data for a year is missing.")
    if np.all(np.isnan(popdata), axis=1).any():
        raise DataConsistencyError("All data for a country is missing.")

    total_pop=np.sum(popdata,axis=0)
    print("Total population for each year:")
    for i ,a in enumerate(total_pop, start=2000): # enumerate gives  index and item
            print("Year ",i," :",a)

    Avg_pop=np.mean(popdata,axis=0)
    print("Average population for each year:")
    for i ,a in enumerate( Avg_pop, start=2000):
            print("Year ",i," :",a)

    std_pop=np.std(popdata,axis=0)
    print("Standard deviation of population for each year:" )
    for i ,a in enumerate( std_pop, start=2000):
            print("Year ",i," :",a)

    population_growth = np.diff(popdata, axis=1)  # Calculate year-to-year difference
    total_growth = np.sum(population_growth, axis=1)  # Sum of growth across all years for each country
    max_growth_country_index = np.argmax(total_growth)
    print("Country with the maximum population growth over the years (index):", max_growth_country_index + 1)

except DataConsistencyError as e:
    print("Data consistency error:", e)
except InvalidDataError as e:
    print("Invalid data error:", e)

#12
'''
(a) Compute the following statistics:
(i) Average score per student.
(ii) Average score per subject.
(iii) Identify students who scored below the passing mark (e.g., 40%) in
any subject.
(iv) Calculate the overall class average.
(b) Missing scores are represented as np.nan and should be ignored.
(c) Raise a ScoresDataError if scores are outside the range 0 to 100.
(d) Ensure the scores data is a 2D NumPy array.
(e) Raise a InvalidScoresDataError if input validation fails.
'''

import numpy as np
class  ScoresDataError(Exception):
    pass
class InvalidScoresDataError(Exception):
    pass

try:
    scores_array = np.array([
    [77, 83, 52, 48, 49, 51],
    [45, 55, 40, 56, 41, 52],
    [47, 85, 100, 46, 65, 90],
    [60, 77, 58, 60, 51, 100],
    [82, 68, 69, 54, 90, 44],
    [63, 63, 81, 89, 95, 70],
    [72, 62, 53, 81, 49, 47],
    [62, 97, 41, 40, 100, 57]])

    if scores_array.ndim != 2:
        raise InvalidScoresDataError("The input data must be a 2D NumPy array.")

    if np.any(scores_array < 0) or np.any(scores_array > 100):
        raise ScoresDataError("Scores must be within the range 0 to 100.")

    average_per_student = np.nanmean(scores_array, axis=1)
    print("Average score per student:")
    for i, avg in enumerate(average_per_student, start=1):
        print(f"Student_{i}: {avg:.2f}")

    average_per_subject = np.nanmean(scores_array, axis=0)
    print("\nAverage score per subject:")
    for i, avg in enumerate(average_per_subject, start=1):
        print(f"Subject_{i}: {avg:.2f}")

    # Identify students who scored below the passing mark (40%) in any subject
    passing_mark = 40
    students_below_passing = np.any(scores_array < passing_mark, axis=1)
    print("\nStudents who scored below the passing mark (40%) in any subject:")
    for i, below_passing in enumerate(students_below_passing, start=1):
        status = "Yes" if below_passing else "No"
        print(f"Student_{i}: {status}")

    # Calculate the overall class average
    overall_class_average = np.nanmean(scores_array) #finding mean excluding nan values
    print(f"\nOverall class average: {overall_class_average:.2f}")

except ScoresDataError as e:
    print(f"Error: {e}")
except InvalidScoresDataError as e:
    print(f"Error: {e}")
