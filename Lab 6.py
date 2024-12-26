import numpy as np
import random

arr=np.dtype([('Employee ID','i4'),('Department','U20'),('Years of Experience','f4'),('Projects completed','i4'),('Client Satisfaction Rating','f4')])
departments=['HR','Marketing','Sales','Fincance','IT']

data = np.zeros(20, dtype=arr)
for i in range(20):
    data[i] = (random.randint(1000, 9999),
               random.choice(departments),
               round(random.uniform(0, 15), 1),
               random.randint(1, 20),
               round(random.uniform(1.0, 5.0), 1))

print(data)

def filterDep(data):
    for i in departments:
        print('\nEmployees working under ',i,'department are:')
        filtered_data = data[data['Department'] == i]
        if len(filtered_data) > 0:
            print(filtered_data)
        else:
            print(" No employees in this department.")

filterDep(data)
print('\nEmployees with Highest Client Satisfaction Rating are:')
f2 = data[data['Client Satisfaction Rating'] == 5.0]
if len(f2) > 0:
    print(f2)
else:
    print(" No employees have Highest Client Satisfaction Rating 5.")

average_pro = np.mean(data['Projects completed'])
print("\nAverage no.of projects completed: ",average_pro)

average_exp = np.mean(data['Years of Experience'])
print("\nAverage years of Experience: ",average_exp)

print("\nEmployees with less than 2 years of experience are: ")
f3 = data[data['Years of Experience'] < 2]
if len(f3) > 0:
    print(f3)
else:
    print(" No employees have less than 2years of experience.")
