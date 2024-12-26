# main_ListOperations.py

from LibraryManager import LibraryManager
from module_ListFunction import find_max, find_min, calculate_sum, calculate_average, find_median
from set_operations import *
from dict_operations import *
from weather_analysis import *

def main():
    while True:
        print("\n--- Menu ---")
        print("1. List Operations")
        print("2. Set Operations")
        print("3. Dictionary Operations")
        print("4. Library Management")
        print("5. Weather Analysis")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            lst = [int(x) for x in input("Enter list elements separated by space: ").split()]
            print("Max:", find_max(lst))
            print("Min:", find_min(lst))
            print("Sum:", calculate_sum(lst))
            print("Average:", calculate_average(lst))
            print("Median:", find_median(lst))

        elif choice == '2':
            s1 = set(map(int, input("Enter elements of set 1 separated by space: ").split()))
            s2 = set(map(int, input("Enter elements of set 2 separated by space: ").split()))
            print("Add Element:", add_element(s1, int(input("Enter element to add: "))))
            print("Remove Element:", remove_element(s1, int(input("Enter element to remove: "))))
            print("Union:", union_sets(s1, s2))
            print("Intersection:", intersection_sets(s1, s2))
            print("Difference:", difference_sets(s1, s2))
            print("Is Subset:", is_subset(s1, s2))
            print("Length of Set:", set_length(s1))
            print("Unique Subsets:", unique_subsets(s1))

        elif choice == '3':
            dict1 = {'a': 1, 'b': 2, 'c': 3}
            dict2 = {'b': 2, 'c': 4, 'd': 5}
            dict3 = {'b': 2, 'c': 3, 'e': 6}
            print("Merged Dictionary:", merging_Dict(dict1, dict2, dict3))
            print("Common Keys:", common_keys(dict1, dict2, dict3))
            print("Inverted Dictionary:", invert_dict(dict1))
        elif choice == '4':
            library = LibraryManager()
            library.add_book("978-3-16-148410-0", "Operating Systems Concepts", "Abraham Silberschatz", "Wiley", "10th", 2021, "978-3-16-148410-0")
            library.add_book("978-0-13-409341-3", "Data Structures and Algorithms in Python", "Michael T. Goodrich", "Wiley", "1st", 2020, "978-0-13-409341-3")
            library.add_book("978-0-262-03384-8", "Machine Learning", "Tom M. Mitchell", "McGraw Hill", "1st", 2021, "978-0-262-03384-8")
            
            print("\n--- Library Management System ---")
            print("All books:", library.list_books())
            print("Searching for 'Machine Learning':", library.search_books("Machine Learning"))
            print("Book details for ISBN '978-3-16-148410-0':", library.get_book("978-3-16-148410-0"))
            library.update_book("978-3-16-148410-0", title="Operating Systems Concepts Updated Edition")
            print("Updated book details for ISBN '978-3-16-148410-0':", library.get_book("978-3-16-148410-0"))
            library.remove_book("978-0-13-409341-3")
            print("All books after removal:", library.list_books())
            print("Is ISBN '978-0-262-03384-8' available?", library.is_available("978-0-262-03384-8"))

        elif choice == '5':
            weather = [
                {"Date": "20th July", "Maximum temperature (in Celsius)": 28, "Minimum temperature (in Celsius)": 25, "Humidity (in percentage)": 77},
                {"Date": "21th July", "Maximum temperature (in Celsius)": 27, "Minimum temperature (in Celsius)": 24, "Humidity (in percentage)": 81},
                {"Date": "22th July", "Maximum temperature (in Celsius)": 27, "Minimum temperature (in Celsius)": 22, "Humidity (in percentage)": 84},
                {"Date": "23th July", "Maximum temperature (in Celsius)": 28, "Minimum temperature (in Celsius)": 25, "Humidity (in percentage)": 76},
                {"Date": "24th July", "Maximum temperature (in Celsius)": 29, "Minimum temperature (in Celsius)": 26, "Humidity (in percentage)": 64},
                {"Date": "25th July", "Maximum temperature (in Celsius)": 28, "Minimum temperature (in Celsius)": 22, "Humidity (in percentage)": 82},
                {"Date": "26th July", "Maximum temperature (in Celsius)": 27, "Minimum temperature (in Celsius)": 24, "Humidity (in percentage)": 81}
            ]
            
            while True:
                print("\n--- Weather Analysis ---")
                print("1. Display Weather Data")
                print("2. Calculate Average Maximum and Minimum Temperatures")
                print("3. Calculate Average Humidity")
                print("4. Back to Main Menu")
                weather_choice = input("Enter your choice: ")
                
                if weather_choice == '1':
                    for day in weather:
                        print("Date: " + day['Date'] + ", Max Temp: " + str(day['Maximum temperature (in Celsius)']) + "°C, Min Temp: " + str(day['Minimum temperature (in Celsius)']) + "°C, Humidity: " + str(day['Humidity (in percentage)']) + "%")

                
                elif weather_choice == '2':
                    avg_temp(weather)
                
                elif weather_choice == '3':
                    avg_humid(weather)
                
                elif weather_choice == '4':
                    break
                
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
