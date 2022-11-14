from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.page import IPage


class MainPage(IPage):
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.url = 'https://hh.ru'

    def open(self):
        self.driver.get(self.url)

    def _is_unauthorized(self):
        return self.driver.find_element[By.CSS_SELECTOR, '[data-qa="login"]']

    def authorize(self):
        if self._is_unauthorized():
            pass
