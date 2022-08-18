from data import google_form_link, zillow_filtered_link
from zillow_scraper import ZillowScraper
from form_filler import FormFiller
import time

# scraper = ZillowScraper(zillow_filtered_link)
# scraper.get_html()
# scraper.make_soup()
# scraper.get_addresses()
# scraper.get_links()
# scraper.get_prices()

test_address = ["Test3", "Test4", "Test5"]
test_link = ["Test3", "Test4", "Test5"]
test_price = ["Test3", "Test4", "Test5"]

filler = FormFiller(google_form_link)
for i in range(0, len(test_address)):
    filler.open_form()
    filler.fill_in(test_address[i], test_price[i], test_link[i])

