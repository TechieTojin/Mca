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

# Step 4: Create a bar plot that shows total precipitation for both stations across the year
plt.figure(figsize=(10, 6))
sns.barplot(x='month', y='precipitation', hue='station', data=monthly_data)
plt.title('Total Precipitation Across the Year by Station')
plt.xlabel('Month')
plt.ylabel('Total Precipitation (mm)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 5: Plot a pie chart showing AQI categories for one station (using station 'ST001' as an example)
# Define AQI categories
def categorize_aqi(aqi):
    if aqi <= 50:
        return 'Good'
    elif 51 <= aqi <= 100:
        return 'Moderate'
    else:
        return 'Unhealthy'

# Apply the categorization for station ST001
data['AQI_category'] = data['air_quality_index'].apply(categorize_aqi)
station_data = data[data['station'] == 'ST001']  # Change to your station ID
aqi_counts = station_data['AQI_category'].value_counts()

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(aqi_counts, labels=aqi_counts.index, autopct='%1.1f%%', colors=['green', 'orange', 'red'], startangle=140)
plt.title('AQI Categories for Station ST001')
plt.show()

# Step 6: Create a scatter plot comparing daily temperature and AQI with color coding
# Define colors for AQI categories
colors = {'Good': 'green', 'Moderate': 'orange', 'Unhealthy': 'red'}

# Plot scatter for station ST001
plt.figure(figsize=(10, 6))
station_scatter_data = station_data.dropna(subset=['temperature', 'air_quality_index'])  # Clean data
plt.scatter(station_scatter_data['temperature'], station_scatter_data['air_quality_index'],
            c=station_scatter_data['AQI_category'].map(colors), alpha=0.7)
plt.title('Temperature vs AQI for Station ST001')
plt.xlabel('Temperature (°C)')
plt.ylabel('Air Quality Index (AQI)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 7: Generate a heatmap showing monthly average AQI levels for both stations
monthly_aqi = data.groupby(['station', 'month']).agg({'air_quality_index': 'mean'}).reset_index()

# Use correct arguments for the pivot function
monthly_aqi_pivot = monthly_aqi.pivot(index='month', columns='station', values='air_quality_index')

# Plot heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(monthly_aqi_pivot, cmap='coolwarm', annot=True, fmt=".1f", cbar_kws={'label': 'AQI'})
plt.title('Monthly Average AQI Levels for Both Stations')
plt.xlabel('Station')
plt.ylabel('Month')
plt.tight_layout()
plt.show()