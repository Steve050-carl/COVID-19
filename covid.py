# 📦 Install dependencies before running:
# pip install requests tabulate

import requests
from tabulate import tabulate

# Function to fetch global COVID-19 data
def get_global_data():
    try:
        url = "https://disease.sh/v3/covid-19/all"
        response = requests.get(url)
        response.raise_for_status()  # Raise error if request fails
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching global data: {e}")
        return None

# Function to fetch COVID-19 data for a specific country
def get_country_data(country):
    try:
        url = f"https://disease.sh/v3/covid-19/countries/{country}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {country}: {e}")
        return None

# Function to display data in a table format
def display_data(data, title):
    if data:
        table = [
            ["Total Cases", data.get("cases")],
            ["Total Deaths", data.get("deaths")],
            ["Total Recovered", data.get("recovered")],
            ["Active Cases", data.get("active")],
            ["Today's Cases", data.get("todayCases")],
            ["Today's Deaths", data.get("todayDeaths")],
        ]
        print(f"\n--- {title} ---")
        print(tabulate(table, headers=["Description", "Count"], tablefmt="pretty"))
    else:
        print("No data available to display.")

# Main menu function
def main():
    print("\n📊 GLOBAL COVID-19 DATA TRACKER 📊\n")
    while True:
        print("\nPlease select an option:")
        print("1. View Global Data")
        print("2. View Country-Specific Data")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            data = get_global_data()
            display_data(data, "Global COVID-19 Statistics")

        elif choice == "2":
            country = input("Enter country name (e.g. Kenya, India, USA): ").lower()
            data = get_country_data(country)
            if data and "message" in data:
                print("❌ Country not found. Please try again.")
            else:
                display_data(data, f"{country.title()} COVID-19 Statistics")

        elif choice == "3":
            print("Thank you for using the COVID-19 Data Tracker. Stay safe! ✌️")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Entry point
if __name__ == "__main__":
    main()
