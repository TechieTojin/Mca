import pandas as pd

# Define functions for each operation

def load_data():
    global covid_data, gdp_data
    covid_data = pd.read_csv('synthetic_covid_data.csv')
    gdp_data = pd.read_csv('synthetic_gdp_data.csv')
    print("Data loaded successfully.")

def display_data():
    print("COVID-19 Data:")
    print(covid_data.head())
    print("\nGDP Data:")
    print(gdp_data.head())

def check_for_duplicates():
    print("\nDuplicate rows in COVID-19 Data: " + str(covid_data.duplicated().sum()))
    print("Duplicate rows in GDP Data: " + str(gdp_data.duplicated().sum()))

def remove_duplicates():
    global covid_data, gdp_data
    covid_data = covid_data.drop_duplicates()
    gdp_data = gdp_data.drop_duplicates()
    print("\nDuplicates removed.")

def add_active_cases():
    global covid_data
    covid_data['active_cases'] = covid_data['confirmed_cases'] - covid_data['recovered']
    print("\nActive cases column added.")

def aggregate_by_quarter():
    global quarterly_covid_data
    covid_data['month'] = pd.to_datetime(covid_data['month'])
    covid_data['quarter'] = covid_data['month'].dt.to_period('Q')
    quarterly_covid_data = covid_data.groupby(['country', 'quarter']).agg({
        'confirmed_cases': 'sum',
        'deaths': 'sum',
        'active_cases': 'sum'
    }).reset_index()
    print("\nCOVID-19 data aggregated by quarter.")

def convert_gdp_quarter():
    global gdp_data
    def convert_to_period(quarter_str):
        try:
            return pd.Period(quarter_str, freq='Q')
        except Exception as e:
            print(f"Error converting {quarter_str} to period: {e}")
            return None

    gdp_data['quarter'] = gdp_data['quarter'].astype(str).apply(convert_to_period)
    gdp_data = gdp_data.dropna(subset=['quarter'])
    print("\nGDP quarter conversion done.")

def merge_datasets():
    global merged_data
    merged_data = pd.merge(quarterly_covid_data, gdp_data, on=['country', 'quarter'])
    print("\nDatasets merged successfully.")
    print(merged_data.head())

def analyze_data():
    country_gdp_growth = merged_data.groupby('country')['gdp_growth'].sum()
    highest_gdp_growth_country = country_gdp_growth.idxmax()
    print("\nThe country with the highest overall GDP growth is: " + highest_gdp_growth_country)

    country_covid_totals = merged_data.groupby('country').agg({
        'confirmed_cases': 'sum',
        'deaths': 'sum'
    })

    highest_cases_country = country_covid_totals['confirmed_cases'].idxmax()
    highest_deaths_country = country_covid_totals['deaths'].idxmax()

    print("\nThe country with the highest total confirmed cases is: " + highest_cases_country)
    print("The country with the highest total deaths is: " + highest_deaths_country)

# Menu-driven interface
def menu():
    while True:
        print("\nMenu:")
        print("1. Load Data")
        print("2. Display Data")
        print("3. Check for Duplicates")
        print("4. Remove Duplicates")
        print("5. Add Active Cases Column")
        print("6. Aggregate COVID-19 Data by Quarter")
        print("7. Convert GDP Quarter to Period")
        print("8. Merge Datasets")
        print("9. Analyze Data")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            load_data()
        elif choice == '2':
            display_data()
        elif choice == '3':
            check_for_duplicates()
        elif choice == '4':
            remove_duplicates()
        elif choice == '5':
            add_active_cases()
        elif choice == '6':
            aggregate_by_quarter()
        elif choice == '7':
            convert_gdp_quarter()
        elif choice == '8':
            merge_datasets()
        elif choice == '9':
            analyze_data()
        elif choice == '10':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()
