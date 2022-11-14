from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.page import Page


class LoginPage(Page):
    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)
        self.url = 'https://hh.ru/account/login'

    def set_login(self):
        pass

    def set_password(self):
        pass

    def press_submit(self):
        pass

    def login(self, login, password):
        pass
