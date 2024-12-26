import numpy as np

dtype = [('EmployeeID', int),('Department', 'U15'),('YearsOfExperience', float),('ProjectsCompleted', int), ('ClientSatisfactionRating', float)]

np.random.seed(0)

num_employees = 20
employee_ids = np.arange(1, num_employees + 1)
departments = np.random.choice(['Engineering', 'HR', 'Marketing', 'Sales'], num_employees)
years_of_experience = np.random.uniform(0, 15, num_employees)
projects_completed = np.random.randint(1, 21, num_employees)
client_satisfaction_ratings = np.random.uniform(1.0, 5.0, num_employees)

data = np.zeros(num_employees, dtype=dtype)
data['EmployeeID'] = employee_ids
data['Department'] = departments
data['YearsOfExperience'] = years_of_experience
data['ProjectsCompleted'] = projects_completed
data['ClientSatisfactionRating'] = client_satisfaction_ratings

def filter_by_department(department_name):
    return data[data['Department'] == department_name]

def highest_client_satisfaction():
    return data[np.argmax(data['ClientSatisfactionRating'])]

def calculate_averages():
    avg_projects = np.mean(data['ProjectsCompleted'])
    avg_experience = np.mean(data['YearsOfExperience'])
    return avg_projects, avg_experience

def less_than_two_years_experience():
    return data[data['YearsOfExperience'] < 2]

if __name__ == "__main__":
    print("Structured Array:")
    print(data)

    print("\nEngineering Employees:")
    print(filter_by_department('Engineering'))

    print("\nEmployee with Highest Client Satisfaction Rating:")
    print(highest_client_satisfaction())

    avg_projects, avg_experience = calculate_averages()