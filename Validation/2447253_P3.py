# Lab-3_menu.py

import qrcode
from PIL import Image
import re
from User_register import *

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
    while True:
        print("\nMenu:")
        print("1. Generate QR Code")
        print("2. Register Equipment from SmartScan")
        print("3. View All Registered Equipment")
        print("4. Exit")

        

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Generate QR Code
            equipment_id = input("Enter the equipment ID: ")
            equipmentName = input("Enter the equipment name: ")
            CompanyEmail = input("Enter the Company email: ")
            data = f"{equipment_id},{equipmentName},{CompanyEmail}"
            generate_qr_code(data, 'user_qr_code.png')
        elif choice == '2':
            # Register User from SmartScan Code
            equipment_id = input("Enter the equipment ID: ")
            equipmentName = input("Enter the equipment name: ")
            CompanyEmail = input("Enter the Company email: ")
            data = f"{equipment_id},{equipmentName},{CompanyEmail}"
            RegisterUserFromSmartScan(data)
        elif choice == '3':
            # View All Registered Users
            print("List of all registered users:")
            for user in fetch_all_equipment_records():
                print(user)
        elif choice == '4':
            # Exit
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
