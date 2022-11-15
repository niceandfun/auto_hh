from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.page import Page


class LoginPage(Page):
    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)
        self.url = 'https://hh.ru/account/login'

    def set_login(self, login):
        login_field = self.driver.find_element(By.CSS_SELECTOR, '[data-qa="login-input-username"]')
        login_field.send_keys(login)

    def set_password(self, password):
        login_field = self.driver.find_element(By.CSS_SELECTOR, '[data-qa="login-input-password"]')
        login_field.send_keys(password)

    def press_submit(self):
        submit_button = self.driver.find_element(By.XPATH, '//span[text()="Войти"]')
        submit_button.click()

    def login(self, login, password):
        self.click_to_button('[data-qa="expand-login-by-password"]')
        self.set_login(login)
        self.set_password(password)
        self.click_to_button('[data-qa="account-login-submit"]')

    def click_to_button(self, text):
        self.driver.find_element(By.CSS_SELECTOR, text).click()
