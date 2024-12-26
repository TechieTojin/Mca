# smartscan1_registration_module.py

# Initialize a list to store user record
equipment_details = []

# Lambda function to create a new user record
create_equipment_record = lambda equipment_id, equipmentName, CompanyEmail: {"equipment_id": equipment_id, "equipmentName": equipmentName, "CompanyEmail": CompanyEmail}

# Lambda function to insert the user record into the list
insert_equipment_record = lambda record: equipment_details.append(record)

# Lambda function to fetch all user records from the list
fetch_all_equipment_records = lambda: equipment_details

def SmartScanCode(data):
    """Decode data from QR code."""
    # Assume data is a comma-separated string: "user_id,name,email"
    try:
        equipment_id, equipmentName, CompanyEmail = data.split(',')
        return equipment_id, equipmentName, CompanyEmail
    except ValueError:
        raise ValueError("Data entered is incorrect.")
