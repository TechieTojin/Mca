import matplotlib.pyplot as plt
import numpy as np

# ----Line Chart------
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]
plt.plot(x, y)
plt.title("Line Chart")
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.show()

# Sine wave plot
x = np.arange(0, 10*np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y, color='green')
plt.show()

# ----------Bar Chart (Students enrolled in different courses)----
data = {'C':20, 'C++':15, 'Java':30, 'Python':35}
x = list(data.keys())
y = list(data.values())
fig = plt.figure(figsize=(5, 5))
plt.bar(x, y, color='maroon', width=0.4)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

# Bar Chart for Monthly Sales of Products in 2023
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
product_a = [120, 150, 170, 160, 180, 190, 200, 210, 220, 230, 240, 250]
product_b = [85, 95, 110, 120, 140, 145, 155, 165, 175, 185, 195, 205]
product_c = [90, 100, 130, 140, 160, 170, 180, 190, 200, 210, 220, 230]
x = np.arange(len(months))
plt.figure(figsize=(10,6))
plt.bar(x - 0.2, product_a, width=0.2, label='Product A', color='b')
plt.bar(x, product_b, width=0.2, label='Product B', color='g')
plt.bar(x + 0.2, product_c, width=0.2, label='Product C', color='r')
plt.xlabel('Months')
plt.ylabel('Sales (in units)')
plt.title('Monthly Sales of Products in 2023')
plt.xticks(x, months, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# ----------Histogram----------
data = np.random.randn(1000)
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')
plt.show()

# Scatter Plot
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.show()

# Scatter plot comparing student performance
subjects = ["Math", "Physics", "Chemistry", "Biology", "English"]
scores_A = [85, 78, 92, 88, 76]
scores_B = [82, 80, 88, 90, 74]
x_values = range(len(subjects))
plt.scatter(x_values, scores_A, color='blue', marker='o', label='Student A')
plt.scatter(x_values, scores_B, color='green', marker='x', label='Student B')
plt.xticks(x_values, subjects)
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.title("Performance Comparison of Two Students")
plt.legend()
plt.show()

# Scatter plot with clusters
x1 = [1, 2, 3, 4, 5]
y1 = [1, 2, 1.5, 3, 2.5]
x2 = [8, 9, 10, 11, 12]
y2 = [7, 8, 8.5, 7.5, 9]
x3 = [5, 6, 7, 8, 9]
y3 = [12, 13, 12.5, 13.5, 14]
plt.scatter(x1, y1, color='blue', marker='o', label='Group A')
plt.scatter(x2, y2, color='green', marker='s', label='Group B')
plt.scatter(x3, y3, color='red', marker='^', label='Group C')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot with Clusters")
plt.legend()
plt.show()

# Randomly generated clusters for scatter plot
np.random.seed(42)
x1 = np.random.normal(5, 1, 30)
y1 = np.random.normal(5, 1, 30)
x2 = np.random.normal(10, 1, 30)
y2 = np.random.normal(10, 1, 30)
x3 = np.random.normal(15, 1, 30)
y3 = np.random.normal(5, 1, 30)
plt.scatter(x1, y1, color='blue', marker='o', label='Group A')
plt.scatter(x2, y2, color='green', marker='s', label='Group B')
plt.scatter(x3, y3, color='red', marker='^', label='Group C')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot with 3 Clusters (30 Data Points Each)")
plt.legend()
plt.show()

# ----------Pie Chart----------
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.3, 0, 0, 0.0]
plt.pie(y, labels=mylabels, explode=myexplode)
plt.show()

# Pie chart for smartphone market share
companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
market_share = [30, 25, 20, 15, 10]
explode = [0.1, 0, 0, 0, 0]
plt.pie(market_share, labels=companies, autopct='%1.1f%%', explode=explode, shadow=True, startangle=140)
plt.title("Market Share of Smartphone Companies")
plt.axis('equal')
plt.show()

# ----------Subplot Example----------
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 1, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 1, 2)
plt.plot(x,y)
plt.show()

# ----------3D Bar Plot----------
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
z = np.zeros(5)
dz = [1, 2, 3, 4, 5]
ax.bar3d(x, y, z, dx=0.5, dy=0.5, dz=dz, color='blue')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('Simple 3D Bar Plot')
plt.show()

# ----------Heatmap----------
data = np.random.random((12, 12))
plt.imshow(data)
plt.title("2-D Heat Map")
plt.show()
