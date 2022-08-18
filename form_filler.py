# Use Selenium to populate the Google form
# Import all the necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# Pip install webdriver_manager
import time


class FormFiller:

    def __init__(self, link):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.link = link

    # Open the form page
    def open_form(self):
        self.driver.get(self.link)

    # Fill in the form with the acquired data
    def fill_in(self, address, price, property_link):
        time.sleep(5)
        address_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]'
                                                           '/div/div[1]/div/div[1]/input')
        address_input.send_keys(address)
        price_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div'
                                                         '/div[1]/div/div[1]/input')
        price_input.send_keys(price)
        link_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/'
                                                        'div[1]/div/div[1]/input')
        link_input.send_keys(property_link)
        send_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/'
                                                         'span/span')
        send_button.click()


