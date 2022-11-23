from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.url = 'https://hh.ru/account/login'

    def _set_login(self, login):
        login_field = self.driver.find_element(*LoginPageLocators.LOGIN_INPUT_FIELD)
        login_field.send_keys(login)

    def _set_password(self, password):
        login_field = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT_FIELD)
        login_field.send_keys(password)

    def _click_submit_button(self):
        self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    def _click_login_by_password_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BY_PASSWORD_BUTTON).click()

    def login(self, login, password):
        self._click_login_by_password_button()
        self._set_login(login)
        self._set_password(password)
        self._click_submit_button()


class LoginPageLocators:
    LOGIN_INPUT_FIELD = (By.CSS_SELECTOR, '[data-qa="login-input-username"]')
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, '[data-qa="login-input-password"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-qa="account-login-submit"]')
    LOGIN_BY_PASSWORD_BUTTON = (By.CSS_SELECTOR, '[data-qa="expand-login-by-password"]')
