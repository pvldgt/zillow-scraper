# Scrape the necessary info with BeautifulSoup
from bs4 import BeautifulSoup
import requests

# Request headers to avoid Zillow Captcha.
# Add your info, see https://www.quora.com/How-do-I-view-HTTP-headers-in-my-web-browser
req_headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/"
              "apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    'upgrade-insecure-requests': '1'
}


# Create the class for the zillow scraper
class ZillowScraper:

    def __init__(self, link):
        self.link = link
        self.zillow_website = ""
        self.soup = None

    # Get the HTML of the page
    def get_html(self):
        response = requests.get(url=self.link, headers=req_headers)
        self.zillow_website = response.text

    # Parse the page
    def make_soup(self):
        self.soup = BeautifulSoup(self.zillow_website, "html.parser")

    # Get the list of addresses
    def get_addresses(self):
        addresses = self.soup.find_all(name="address")
        address_list = [address.getText() for address in addresses]
        return address_list

    # Get the list of links
    def get_links(self):
        links = self.soup.find_all('a', {"data-test": "property-card-link"}, href=True)
        link_list = []
        for link in links:
            if "https://www.zillow.com/" in link["href"]:
                if link["href"] not in link_list:
                    link_list.append(link["href"])
            else:
                if "https://www.zillow.com"+link["href"] not in link_list:
                    link_list.append("https://www.zillow.com"+link["href"])
        return link_list

    # Get the list of prices
    def get_prices(self):
        prices = self.soup.find_all("span", {"data-test": "property-card-price"})
        price_list = []
        for price in prices:
            placeholder = price.getText()[:6].strip("$").replace(",", "")
            price_list.append(int(placeholder))
        return price_list
