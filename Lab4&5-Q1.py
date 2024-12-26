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
        return "MRI Equipment " + self.equipment_id + " has a " + str(int(failure_probability * 100)) + "% chance of failure."

class CTScanner(MedicalEquipment):
    def predict_failure(self):
        days_since_last_service = (datetime.now() - self.last_service_date).days
        failure_probability = min(0.8, days_since_last_service / 800)
        return "CT Scanner " + self.equipment_id + " has a " + str(int(failure_probability * 100)) + "% chance of failure."

class Ultrasound(MedicalEquipment):
    def predict_failure(self):
        days_since_last_service = (datetime.now() - self.last_service_date).days
        failure_probability = min(0.7, days_since_last_service / 600)
        return "Ultrasound " + self.equipment_id + " has a " + str(int(failure_probability * 100)) + "% chance of failure."

# Instantiate and store in a list
equipment_list = [
    MRI("MRI123", datetime.now() - timedelta(days=500)),
    CTScanner("CT456", datetime.now() - timedelta(days=300)),
    Ultrasound("US789", datetime.now() - timedelta(days=200))
]

# Demonstrate polymorphism
for equipment in equipment_list:
    print(equipment.predict_failure())
