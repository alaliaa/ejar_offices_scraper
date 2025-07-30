
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_ejar(url, number_of_pages,save_to_csv=False):
    """
    Scrapes brokerage office data from the given URL and returns it as a list of dictionaries.
    """
    try:
        all_offices = []
        base_url = url

        for page in range(0, number_of_pages):
            page_url = f"{base_url}&page={page}"
            print(f"Scraping page {page + 1}: {page_url}")

            try:
                response = requests.get(page_url)
                response.raise_for_status()
                response.encoding = 'utf-8'
            except requests.exceptions.RequestException as e:
                print(f"Could not scrape page {page + 1}: {e}")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')

            offices_on_page = soup.find_all('div', class_='views-row')
            if not offices_on_page:
                print(f"No more offices found on page {page + 1}. Stopping.")
                break

            for office_div in offices_on_page:
                name_div = office_div.find('div', class_='views-field-field-bo-name')
                name = name_div.find('a').get_text(strip=True) if name_div and name_div.find('a') else 'N/A'

                region_div = office_div.find('div', class_='views-field-field-bo-region')
                region = region_div.find('div', class_='field-content').get_text(strip=True) if region_div and region_div.find('div', class_='field-content') else 'N/A'

                city_div = office_div.find('div', class_='views-field-field-bo-city')
                city = city_div.find('div', class_='field-content').get_text(strip=True) if city_div and city_div.find('div', class_='field-content') else 'N/A'

                district_div = office_div.find('div', class_='views-field-field-bo-district')
                district = district_div.find('div', class_='field-content').get_text(strip=True) if district_div and district_div.find('div', class_='field-content') else 'N/A'

                phone_div = office_div.find('div', class_='views-field-field-bo-phone')
                phone = phone_div.find('div', class_='field-content').get_text(strip=True) if phone_div and phone_div.find('div', class_='field-content') else 'N/A'

                rating_div = office_div.find('div', class_='views-field-field-bo-rating-count')
                rating = rating_div.find('b').get_text(strip=True) if rating_div and rating_div.find('b') else 'N/A'

                all_offices.append({
                    'Name': name,
                    'District': district,
                    'Phone': phone,
                    'Rating': rating
                })
        
        if not all_offices:
            print("No offices found.")
            return None

        if save_to_csv: 
            df = pd.DataFrame(all_offices)
            df.to_csv('ejar_offices.csv', index=False)
        
        return all_offices

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None