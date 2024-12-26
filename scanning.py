# scanning.py
# DOMAIN:Medical Equipment Failure Prediction
import qrcode
from PIL import Image
import re
from User_register import RegisterUserFromSmartScan

def is_valid_equipment_id(equipment_id):
    """Validate equipment ID."""
    return len(equipment_id) > 0

def is_valid_equipmentName(equipmentName):
    """Validate equipment name to ensure it contains only letters and spaces."""
    return bool(re.match(r"^[A-Za-z\s]+$", equipmentName))

def is_valid_CompanyEmail(CompanyEmail):
    """Validate Company Email address format."""
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", CompanyEmail))

def generate_qr_code(data, filename='user_qr_code.png'):
    """Generate a QR code from the given data and save it to a file."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR code saved as {filename}")

    # Display the QR code image
    img.show()

def main():
    # User details
    equipment_id = input("Enter the equipment ID: ")
    equipmentName = input("Enter the equipment name: ")
    CompanyEmail = input("Enter the Company email: ")

    # Validate user input
    if not is_valid_equipment_id(equipment_id):
        print("Invalid equipment ID. It should not be empty.")
        return

    if not is_valid_equipmentName(equipmentName):
        print("Invalid equipment name. It should contain only letters and spaces.")
        return

    if not is_valid_CompanyEmail(CompanyEmail):
        print("Invalid Company email format.")
        return

    # Combine details into a comma-separated string
    data = f"{equipment_id},{equipmentName},{CompanyEmail}"

    # Generate QR code
    generate_qr_code(data, 'user_qr_code.png')

    # Register user from QR code data
    RegisterUserFromSmartScan(data)

if __name__ == "__main__":
    main()
