
import streamlit as st
import requests

def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"  # Corrected URL
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country_data = data[0]
        name = country_data["name"]["common"]
        capital = country_data.get("capital", ["N/A"])[0]
        population = country_data.get("population", "N/A")
        area = country_data.get("area", "N/A")
        region = country_data.get("region", "N/A")
        
        # Handle currency (nested dict)
        currencies = country_data.get("currencies", {})
        if currencies:
            currency = ", ".join([f"{v['name']} ({k})" for k, v in currencies.items()])
        else:
            currency = "N/A"
        
        return name, capital, population, area, currency, region
    else:
        return None

def main():
    st.title("Welcome to Join Us")
    st.subheader("🌍 Country Information App")

    country_name = st.text_input("Enter country name: ")

    if country_name:
        country_info = fetch_country_data(country_name)
        if country_info:
            name, capital, population, area, currency, region = country_info
            st.subheader("📌 Country Information")
            st.write(f"**Name:** {name}")
            st.write(f"**Capital:** {capital}")
            st.write(f"**Population:** {population:,}")
            st.write(f"**Area:** {area:,} km²")
            st.write(f"**Currency:** {currency}")
            st.write(f"**Region:** {region}")
        else:
            st.error("❌ Country data not found. Please check the name and try again.")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: grey;'>Created by Afia Bakr</h5>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

