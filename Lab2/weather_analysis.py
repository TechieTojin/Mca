'''
(5) Write a Python program for a wether analyzing system to process and analyze
weather data for Bangalore City from 20th July to 26th July in 2024.
(a) Each day’s data includes:
• Date
• Maximum temperature (in Celsius)
• Minimum temperature (in Celsius)
• Humidity (in percentage)
[Hint: The data may be stored in a list of dictionaries]

(b) Write a function that finds the average maximum and minimum temperatures from the weather data.

(c) Write a function that calculates the average humidity over the given period
'''
#a
weather=[{"Date":"20th July","Maximum temperature (in Celsius)":28,"Minimum temperature (in Celsius)":25,"Humidity (in percentage)":77},
         {"Date":"21th July","Maximum temperature (in Celsius)":27,"Minimum temperature (in Celsius)":24,"Humidity (in percentage)":81},
         {"Date":"22th July","Maximum temperature (in Celsius)":27,"Minimum temperature (in Celsius)":22,"Humidity (in percentage)":84},
         {"Date":"23th July","Maximum temperature (in Celsius)":28,"Minimum temperature (in Celsius)":25,"Humidity (in percentage)":76},
         {"Date":"24th July","Maximum temperature (in Celsius)":29,"Minimum temperature (in Celsius)":26,"Humidity (in percentage)":64},
         {"Date":"25th July","Maximum temperature (in Celsius)":28,"Minimum temperature (in Celsius)":22,"Humidity (in percentage)":82},
         {"Date":"26th July","Maximum temperature (in Celsius)":27,"Minimum temperature (in Celsius)":24,"Humidity (in percentage)":81}]

#b
def avg_temp(weather):
    sum1=sum2=0
    for i in weather:
            sum1+=i["Maximum temperature (in Celsius)"]
            sum2+=i["Minimum temperature (in Celsius)"]
    avg1=sum1/7
    avg2=sum2/7
    print("the average maximum temperature from the weather data is :",avg1)
    print("the average minimum temperature from the weather data is :",avg2)
avg_temp(weather)
#c
def avg_humid(weather):
    sum=0
    for i in weather:
        sum+=i["Humidity (in percentage)"]
    avg=sum/7
    print("the average humidity over the given period is:",avg)
avg_humid(weather)
