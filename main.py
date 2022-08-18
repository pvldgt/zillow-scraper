from data import google_form_link, zillow_filtered_link
from zillow_scraper import ZillowScraper

scraper = ZillowScraper(zillow_filtered_link)
scraper.get_html()
scraper.make_soup()
scraper.get_addresses()
scraper.get_links()
scraper.get_prices()

