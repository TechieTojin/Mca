#2447253 TOJIN VARKEY SIMSON LAB-1 EXERCISE

import math

while True:
    print("\nMenu:")
    print("1. Perform list operations (sum, multiply, largest, smallest)")
    print("2. Print strings with identical first and last characters")
    print("3. Print patterns")
    print("4. Convert list to a list of dictionaries")
    print("5. Print even numbers and their squares (1-50)")
    print("6. Print even numbers and their squares (1-100)")
    print("7. Sum and reverse digits of a four-digit number")
    print("8. Calculate the area of two triangles and their percentage contribution")
    print("9. Print person information from a dictionary")
    print("10. Extract last elements from a tuple")
    print("11. Find the number of days in a month")
    print("12. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        l1 = [14, 31, 8, 34, 30, 12, 10]
        print("Sum of all the items of the list:", sum(l1))

        prod = 1
        for i in l1:
            prod *= i
        print("Product of all the items:", prod)

        print("The largest number from the list is:", max(l1))
        print("The smallest number from the list is:", min(l1))
    elif choice == '2':
        A = ["abc", "xyz", "aba", "1221"]
        print("The strings with identical first and last characters:")
        for i in A:
            if i[0] == i[-1]:
                print(i)
    elif choice == '3':
        rows = 5
        for i in range(rows):
            print(' ' * (rows - i - 1) + ' '.join(chr(65 + j) for j in range(i + 1)))
        print()
        for i in range(1, rows + 1):
            print("* " * i)
    elif choice == '4':
        color_names = ["Black", "Red", "Maroon", "Yellow"]
        color_codes = ["000000", "FF0000", "800000", "FFFF00"]
        color_list = [{'colorName': color_names[i], 'colorCode': color_codes[i]} for i in range(len(color_names))]
        for color in color_list:
            print(color)
    elif choice == '5':
        for i in range(1, 51):
            if i % 2 == 0:
                print(f"Even number: {i}, Square: {i**2}")
    elif choice == '6':
        for i in range(1, 101):
            if i % 2 == 0:
                print(f"Even number: {i}, Square: {i**2}")
    elif choice == '7':
        n = input("Enter a four-digit number: ")
        sum_digits = sum(int(digit) for digit in n)
        rev = int(n[::-1])
        print("Sum of digits:", sum_digits)
        print("Reverse of digits:", rev)
    elif choice == '8':
        def area(a, b, c):
            s = (a + b + c) / 2
            return math.sqrt(s * (s - a) * (s - b) * (s - c))

        a1, b1, c1 = map(float, input("Enter sides of first triangle (a b c): ").split())
        a2, b2, c2 = map(float, input("Enter sides of second triangle (a b c): ").split())

        area1 = area(a1, b1, c1)
        area2 = area(a2, b2, c2)
        total_area = area1 + area2
        print(f"Area of first triangle: {area1:.2f}")
        print(f"Area of second triangle: {area2:.2f}")
        print(f"Total area: {total_area:.2f}")
        print(f"Contribution of first triangle: {area1/total_area*100:.2f}%")
        print(f"Contribution of second triangle: {area2/total_area*100:.2f}%")
    elif choice == '9':
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
        for person in people:
            print(f"Name: {person['name']}, Age: {person['age']}, Blood Group: {person['blood_group']}")
    elif choice == '10':
        t = ("python", "learn", "includehelp")
        print("Last characters of each string in the tuple:", [i[-1] for i in t])
    elif choice == '11':
        month_days_map = {
            "january": 31, "march": 31, "may": 31, "july": 31, "august": 31, "october": 31, "december": 31,
            "april": 30, "june": 30, "september": 30, "november": 30
        }
        month = input("Enter the month name: ").lower()
        if month in month_days_map:
            print(f"Number of days in {month.capitalize()} is {month_days_map[month]}.")
        elif month == "february":
            year = int(input("Enter the year: "))
            days = 29 if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)) else 28
            print(f"Number of days in February {year} is {days}.")
        else:
            print("Invalid month name.")
    elif choice == '12':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
