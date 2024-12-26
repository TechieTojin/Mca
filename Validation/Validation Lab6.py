import numpy as np
import random

# Define the structured array for employees
arr = np.dtype([('Employee ID', 'i4'),
                ('Department', 'U20'),
                ('Years of Experience', 'f4'),
                ('Projects completed', 'i4'),
                ('Client Satisfaction Rating', 'f4')])

# Departments list
departments = ['HR', 'Marketing', 'Sales', 'Finance', 'IT']

# Generate random data for 20 employees
data = np.zeros(20, dtype=arr)
for i in range(20):
    data[i] = (random.randint(1000, 9999),
               random.choice(departments),
               round(random.uniform(0, 15), 1),
               random.randint(1, 20),
               round(random.uniform(1.0, 5.0), 1))

# Function to display the menu
def display_menu():
    print("\n--- Employee Performance System ---")
    print("1. View all Employee Records")
    print("2. Filter by Department")
    print("3. Employee with Highest Client Satisfaction Rating")
    print("4. Calculate Average Projects Completed and Years of Experience")
    print("5. Employees with Less than 2 Years of Experience")
    print("6. Exit")

# Function to filter and return records by department
def filter_by_department(dept):
    filtered_data = data[data['Department'] == dept]
    if len(filtered_data) > 0:
        print(f"\nEmployees working in {dept} department:")
        print(filtered_data)
    else:
        print(f"No employees found in {dept} department.")

# Function to find the employee(s) with the highest client satisfaction rating
def highest_client_satisfaction():
    max_rating = np.max(data['Client Satisfaction Rating'])
    employees_with_max_rating = data[data['Client Satisfaction Rating'] == max_rating]
    if len(employees_with_max_rating) > 0:
        print("\nEmployee(s) with the highest Client Satisfaction Rating:")
        print(employees_with_max_rating)
    else:
        print("No employees found with the highest satisfaction rating.")

# Function to calculate and display the average number of projects completed and years of experience
def calculate_averages():
    avg_projects = np.mean(data['Projects completed'])
    avg_experience = np.mean(data['Years of Experience'])
    print(f"\nAverage number of projects completed: {avg_projects:.2f}")
    print(f"Average years of experience: {avg_experience:.2f}")

# Function to find employees with less than 2 years of experience
def employees_with_less_experience():
    filtered_data = data[data['Years of Experience'] < 2]
    if len(filtered_data) > 0:
        print("\nEmployees with less than 2 years of experience:")
        print(filtered_data)
    else:
        print("No employees found with less than 2 years of experience.")

# Main loop for menu-driven system
while True:
    display_menu()
    choice = input("\nEnter your choice (1-6): ")

    if choice == '1':
        print("\nAll Employee Records:")
        print(data)

    elif choice == '2':
        print("\nAvailable Departments: ", departments)
        dept_choice = input("Enter the department you want to filter: ")
        if dept_choice in departments:
            filter_by_department(dept_choice)
        else:
            print("Invalid department. Please try again.")

    elif choice == '3':
        highest_client_satisfaction()

    elif choice == '4':
        calculate_averages()

    elif choice == '5':
        employees_with_less_experience()

    elif choice == '6':
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
