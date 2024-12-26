import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
data = pd.read_excel("env_data.xlsx")

# Step 2: Convert the date column to datetime type with the correct format
data['date'] = pd.to_datetime(data['date'], format='%d-%m-%Y')

# Step 3: Group the data by station and calculate monthly average temperature and total precipitation
data['month'] = data['date'].dt.to_period('M')
monthly_data = data.groupby(['station', 'month']).agg({
    'temperature': 'mean',
    'precipitation': 'sum'
}).reset_index()


# Define AQI categories
def categorize_aqi(aqi):
    if aqi <= 50:
        return 'Good'
    elif 51 <= aqi <= 100:
        return 'Moderate'
    else:
        return 'Unhealthy'


# Apply AQI categorization
data['AQI_category'] = data['air_quality_index'].apply(categorize_aqi)


# Function to create bar plot for total precipitation
def plot_precipitation():
    plt.figure(figsize=(10, 6))
    sns.barplot(x='month', y='precipitation', hue='station', data=monthly_data)
    plt.title('Total Precipitation Across the Year by Station')
    plt.xlabel('Month')
    plt.ylabel('Total Precipitation (mm)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Function to create a pie chart for AQI categories
def plot_aqi_pie_chart(station_id):
    station_data = data[data['station'] == station_id]
    aqi_counts = station_data['AQI_category'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(aqi_counts, labels=aqi_counts.index, autopct='%1.1f%%',
            colors=['green', 'orange', 'red'], startangle=140)
    plt.title(f'AQI Categories for Station {station_id}')
    plt.show()


# Function to create a scatter plot for temperature vs AQI
def plot_temperature_vs_aqi(station_id):
    colors = {'Good': 'green', 'Moderate': 'orange', 'Unhealthy': 'red'}
    station_data = data[data['station'] == station_id].dropna(subset=['temperature', 'air_quality_index'])

    plt.figure(figsize=(10, 6))
    plt.scatter(station_data['temperature'], station_data['air_quality_index'],
                c=station_data['AQI_category'].map(colors), alpha=0.7)
    plt.title(f'Temperature vs AQI for Station {station_id}')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Air Quality Index (AQI)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Function to create a heatmap for monthly average AQI levels
def plot_aqi_heatmap():
    monthly_aqi = data.groupby(['station', 'month']).agg({'air_quality_index': 'mean'}).reset_index()
    monthly_aqi_pivot = monthly_aqi.pivot(index='month', columns='station', values='air_quality_index')

    plt.figure(figsize=(10, 6))
    sns.heatmap(monthly_aqi_pivot, cmap='coolwarm', annot=True, fmt=".1f", cbar_kws={'label': 'AQI'})
    plt.title('Monthly Average AQI Levels for Both Stations')
    plt.xlabel('Station')
    plt.ylabel('Month')
    plt.tight_layout()
    plt.show()


# Menu function
def menu():
    while True:
        print("\n--- Data Visualization Menu ---")
        print("1. Total Precipitation Across the Year by Station")
        print("2. Pie Chart of AQI Categories for a Station")
        print("3. Temperature vs AQI Scatter Plot for a Station")
        print("4. Monthly Average AQI Heatmap for Both Stations")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            plot_precipitation()
        elif choice == '2':
            station_id = input("Enter the station ID (e.g., ST001): ")
            plot_aqi_pie_chart(station_id)
        elif choice == '3':
            station_id = input("Enter the station ID (e.g., ST001): ")
            plot_temperature_vs_aqi(station_id)
        elif choice == '4':
            plot_aqi_heatmap()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


# Run the menu
menu()
