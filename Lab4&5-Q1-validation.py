from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Abstract Base Class
class MedicalEquipment(ABC):
    def __init__(self, equipment_id, last_service_date):
        self.equipment_id = equipment_id
        self.last_service_date = last_service_date
    
    @abstractmethod
    def predict_failure(self):
        """Predict the likelihood of equipment failure."""
        pass

# Subclasses
class MRI(MedicalEquipment):
    def predict_failure(self):
        days_since_last_service = (datetime.now() - self.last_service_date).days
        failure_probability = min(0.9, days_since_last_service / 1000)
        return f"MRI Equipment {self.equipment_id} has a {int(failure_probability * 100)}% chance of failure."

class CTScanner(MedicalEquipment):
    def predict_failure(self):
        days_since_last_service = (datetime.now() - self.last_service_date).days
        failure_probability = min(0.8, days_since_last_service / 800)
        return f"CT Scanner {self.equipment_id} has a {int(failure_probability * 100)}% chance of failure."

class Ultrasound(MedicalEquipment):
    def predict_failure(self):
        days_since_last_service = (datetime.now() - self.last_service_date).days
        failure_probability = min(0.7, days_since_last_service / 600)
        return f"Ultrasound {self.equipment_id} has a {int(failure_probability * 100)}% chance of failure."

# Global list to store equipment
equipment_list = []

def display_menu():
    """Display the menu options."""
    print("\n--- Medical Equipment Failure Prediction System ---")
    print("1. Add New Equipment")
    print("2. View Failure Predictions")
    print("3. Exit")

def add_equipment():
    """Add new equipment to the system."""
    try:
        equipment_id = input("Enter Equipment ID: ")
        last_service_date_str = input("Enter Last Service Date (YYYY-MM-DD): ")
        last_service_date = datetime.strptime(last_service_date_str, "%Y-%m-%d")
        
        print("Select Equipment Type:")
        print("1. MRI")
        print("2. CT Scanner")
        print("3. Ultrasound")
        equipment_type = input("Enter choice: ")

        if equipment_type == "1":
            equipment = MRI(equipment_id, last_service_date)
        elif equipment_type == "2":
            equipment = CTScanner(equipment_id, last_service_date)
        elif equipment_type == "3":
            equipment = Ultrasound(equipment_id, last_service_date)
        else:
            print("Invalid equipment type.")
            return

        equipment_list.append(equipment)
        print("Equipment added successfully.")

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def view_predictions():
    """View failure predictions for all equipment."""
    if not equipment_list:
        print("No equipment available.")
        return
    
    for equipment in equipment_list:
        print(equipment.predict_failure())

def main():
    """Main function to run the menu-driven program."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_equipment()
        elif choice == "2":
            view_predictions()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter")

if __name__ == "__main__":
    main()
