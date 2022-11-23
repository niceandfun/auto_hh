from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self):
        super().__init__()
        self.url = 'https://hh.ru'

    def is_unauthorized(self):
        return self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)


class MainPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-qa="login"]')
