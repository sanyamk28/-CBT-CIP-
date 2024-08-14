import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url, output_csv):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Parse the HTML content of the website
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the relevant data - this example assumes data is in table rows
    table_rows = soup.find_all('tr')
    
    # Open a CSV file to write the scraped data
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Iterate over the rows and write them to the CSV file
        for row in table_rows:
            columns = row.find_all('td')
            csvwriter.writerow([column.get_text(strip=True) for column in columns])

    print(f"Data successfully scraped and stored in {output_csv}")

# Example usage
scrape_website('https://example.com', 'output.csv')
