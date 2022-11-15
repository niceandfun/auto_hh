from selenium.webdriver.common.by import By

from pages.page import Page


class MainPage(Page):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = 'https://hh.ru'

    def is_unauthorized(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-qa="login"]')
