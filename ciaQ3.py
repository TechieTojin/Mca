class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def get_details(self):
        return "Name: " + self.name + ", Employee ID: " + self.employee_id
class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def get_details(self):
        base_details = super().get_details()
        return base_details + ", Team Size: " + str(self.team_size)
class Engineer(Employee):
    def __init__(self, name, employee_id, specialization):
        super().__init__(name, employee_id)
        self.specialization = specialization

    def get_details(self):
        base_details = super().get_details()
        return base_details + ", Specialization: " + self.specialization
manager = Manager("ABC", "MCA121", 10)
engineer = Engineer("DEF", "MCA112", "xxxx")


print(manager.get_details())  
print(engineer.get_details())  
