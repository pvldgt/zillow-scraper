# Populate the google_form_link and zillow_filtered_link variable with your own links
from data import google_form_link, zillow_filtered_link
from zillow_scraper import ZillowScraper
from form_filler import FormFiller

# Scrape Zillow for property address, price and link
scraper = ZillowScraper(zillow_filtered_link)
scraper.get_html()
scraper.make_soup()
addresses = scraper.get_addresses()
prices = scraper.get_prices()
links = scraper.get_links()

# Fill in your Google form, the results can be seen in the spreadsheet
filler = FormFiller(google_form_link)
for i in range(0, len(addresses)):
    filler.open_form()
    filler.fill_in(addresses[i], prices[i], links[i])

