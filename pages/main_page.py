from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.url = 'https://hh.ru'

    def open(self):
        self.driver.get(self.url)

    def is_authorized(self):
        return self.driver.find_element[By.CSS_SELECTOR, '[data-qa="login"]']