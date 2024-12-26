import pandas as pd

covid_data = pd.read_csv('synthetic_covid_data.csv')
gdp_data = pd.read_csv('synthetic_gdp_data.csv')

print("COVID-19 Data:")
print(covid_data.head())
print("\nGDP Data:")
print(gdp_data.head())

covid_data['month'] = pd.to_datetime(covid_data['month'])

print("\nDuplicate rows in COVID-19 Data: " + str(covid_data.duplicated().sum()))
print("Duplicate rows in GDP Data: " + str(gdp_data.duplicated().sum()))

covid_data = covid_data.drop_duplicates()
gdp_data = gdp_data.drop_duplicates()

covid_data['active_cases'] = covid_data['confirmed_cases'] - covid_data['recovered']

covid_data['quarter'] = covid_data['month'].dt.to_period('Q')

quarterly_covid_data = covid_data.groupby(['country', 'quarter']).agg({
    'confirmed_cases': 'sum',
    'deaths': 'sum',
    'active_cases': 'sum'
}).reset_index()

def convert_to_period(quarter_str):
    try:
        return pd.Period(quarter_str, freq='Q')
    except Exception as e:
        print(f"Error converting {quarter_str} to period: {e}")
        return None

gdp_data['quarter'] = gdp_data['quarter'].astype(str).apply(convert_to_period)

gdp_data = gdp_data.dropna(subset=['quarter'])

merged_data = pd.merge(quarterly_covid_data, gdp_data, on=['country', 'quarter'])

print("\nMerged Data:")
print(merged_data.head())

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
