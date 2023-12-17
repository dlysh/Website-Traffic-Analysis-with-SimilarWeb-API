# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:46:50 2023

@author: dlysh
"""

import requests
import pandas as pd

# Specify API key 
api_key = "Add_Your_API_KEY"

# Specify date range for the request
start_date = "2020-11"
end_date = "2023-11"

# Specify other parameters
country = "world"  # "gb" for the UK, "world" for worldwide
granularity = "monthly" #Set the granularity for the returned values. Can be 'daily', 'weekly' or 'monthly'.
main_domain_only = False #"True" - subdomains excluded, "False" - included
format_type = "json" 
# OPTIONAL 
show_verified = False
mtd = False
engaged_only = False

def get_website_data(website, headers):
    try:
        # Construct the complete URL with parameters, including base_url and endpoint
        url = f"https://api.similarweb.com/v1/website/{website}/total-traffic-and-engagement/visits?api_key={api_key}&start_date={start_date}&end_date={end_date}&country={country}&granularity={granularity}&main_domain_only={main_domain_only}&format={format_type}&show_verified={show_verified}&mtd={mtd}&engaged_only={engaged_only}"

        # Make the request
        response = requests.get(url, headers=headers)

        # Check if the response is valid (status code 200)
        if response.status_code == 200:
            return website, response.json()
        else:
            print(f"Skipping {website} due to invalid response (Status Code: {response.status_code})")
            return None
    except Exception as e:
        print(f"Skipping {website} due to an error: {e}")
        return None

# Get a list of websites from user input
websites_input = input("Please enter a list of websites separated by a new line:\n")
websites = websites_input.strip().split("\n")

# Define headers
headers = {"accept": "application/json"}

# Dictionary to store website data
website_data = {}
# List to store websites with errors
error_websites = []

# Iterate through each website and get data
for website in websites:
    result = get_website_data(website, headers)
    if result:
        website_data[result[0]] = result[1]
    else:
        error_websites.append(website)

# Create a DataFrame for the table
df = pd.DataFrame()

# Iterate through each website's data
for website, data in website_data.items():
    # Extract dates and visits from the JSON response
    dates = [entry['date'] for entry in data['visits']]
    visits = [entry['visits'] for entry in data['visits']]

    # Create a DataFrame for the current website
    df_website = pd.DataFrame({website: visits}, index=dates)

    # Merge the current website's DataFrame with the main DataFrame
    df = pd.concat([df, df_website], axis=1)

# Save DataFrame to Excel file
with pd.ExcelWriter('total_visits_data.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Data', index_label='Date')
    if error_websites:
        pd.DataFrame({'No available data for': error_websites}).to_excel(writer, sheet_name='Errors', index=False)

# Print the DataFrame
print(df)