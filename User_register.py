# User_register.py

from smartscan_registration_module import *

def RegisterUserFromSmartScan(data):
    """Register a new user from SmartScan Code data."""
    equipment_id, equipmentName, CompanyEmail = SmartScanCode(data)

    # Create a new equipment record
    new_equipment = create_equipment_record(equipment_id, equipmentName, CompanyEmail)
    print(f"Created record: {new_equipment}")

    # Insert user record into the list
    insert_equipment_record(new_equipment)

    # Print all registered users
    print("The list of all registered users after adding the new user:")
    for equipment in fetch_all_equipment_records():
        print(equipment)


