## Create google form (address, price, link)
google_form_link = "https://forms.gle/8mVWxfjd3o3x155CA"

## Filter what you are looking for
zillow_filtered_link = "https://www.zillow.com/portland-or/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Portland%2C%20OR%22%2C%22mapBounds%22%3A%7B%22west%22%3A-123.1688842787086%2C%22east%22%3A-122.22131347792735%2C%22south%22%3A45.26625833936116%2C%22north%22%3A45.84322052818074%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A13373%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A275333%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A1200%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"

## Scrape the necessary info with BeautifulSoup
from bs4 import BeautifulSoup
import requests

# request headers to avoid Zillow Captcha
req_headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    'upgrade-insecure-requests': '1'
}

# Get the HTML of the page
response = requests.get(url=zillow_filtered_link, headers=req_headers)
zillow_website = response.text
# Parse the page
soup = BeautifulSoup(zillow_website, "html.parser")
# print(soup)
addresses = soup.find_all(name="address")
address_list = [address.getText() for address in addresses]

links = soup.find_all('a', {"data-test": "property-card-link"}, href=True)

# link_list = [link["href"] for link in links]
link_list = []
for link in links:
    if "https://www.zillow.com/" in link["href"]:
        link_list.append(link["href"])
    else:
        link_list.append("https://www.zillow.com"+link["href"])
#
# print(link_list)
# print(len(link_list))




## Use Selenium to populate the Google form