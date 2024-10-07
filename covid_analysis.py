import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# URL to the CSV file
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

# Read the dataset into a Pandas DataFrame
covid_data = pd.read_csv(url)

# Display the first few rows
print(covid_data.head())

# Reshape the DataFrame so that each row is a country and date
covid_data_melted = covid_data.melt(
    id_vars=["Province/State", "Country/Region", "Lat", "Long"],
    var_name="Date",
    value_name="Confirmed"
)

# Convert the 'Date' column to a datetime format
covid_data_melted["Date"] = pd.to_datetime(covid_data_melted["Date"])

# Group by country and date to get the total confirmed cases per country/region
covid_data_grouped = covid_data_melted.groupby(["Country/Region", "Date"])["Confirmed"].sum().reset_index()

# Preview the transformed data
print(covid_data_grouped.head())

# Filter data for Canada
canada_data = covid_data_grouped[covid_data_grouped["Country/Region"] == "Canada"]

# Preview the filtered data
print(canada_data.head())

# Calculate daily new cases
canada_data.loc[:, "Daily New Cases"] = canada_data["Confirmed"].diff()

# Preview the data
print(canada_data.tail())

'''
# Plot cumulative confirmed cases over time
plt.figure(figsize=(10, 6))
plt.plot(canada_data["Date"], canada_data["Confirmed"], label="Cumulative Confirmed Cases", color="blue")
plt.title("Cumulative COVID-19 Cases in Canada")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()'''


'''
# Plot daily new cases
plt.figure(figsize=(10, 6))
plt.plot(canada_data["Date"], canada_data["Daily New Cases"], label="Daily New Cases", color="red")
plt.title("Daily New COVID-19 Cases in Canada")
plt.xlabel("Date")
plt.ylabel("Number of New Cases")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()'''

'''
# Filter data for multiple countries
countries = ['Canada', 'India', 'Brazil']
multi_country_data = covid_data_grouped[covid_data_grouped["Country/Region"].isin(countries)]

# Plot data for multiple countries
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = multi_country_data[multi_country_data["Country/Region"] == country]
    plt.plot(country_data["Date"], country_data["Confirmed"], label=country)

plt.title("Cumulative COVID-19 Cases in Selected Countries")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()'''


'''
countries = ['US', 'France', 'China', 'South Africa', 'Australia']
latest_date = covid_data_grouped["Date"].max()
multi_country_data = covid_data_grouped[covid_data_grouped["Country/Region"].isin(countries) & (covid_data_grouped["Date"] == latest_date)]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(multi_country_data["Confirmed"], labels=multi_country_data["Country/Region"], autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Total Confirmed COVID-19 Cases")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()'''