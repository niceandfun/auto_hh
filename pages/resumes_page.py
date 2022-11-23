from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ResumesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://hh.ru/applicant/resumes'

    def update_resume(self):
        self.driver.find_element(*ResumesPageLocators.UPDATE_BUTTON)


class ResumesPageLocators:
    UPDATE_BUTTON = (By.CSS_SELECTOR, '[data-qa-title="QA Engineer"] [data-qa="resume-update-button_actions"]')
