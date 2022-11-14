from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from pages.page import Page


class ResumesPage(Page):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = 'https://hh.ru/applicant/resumes'

    def update_resume(self, title):
        self.driver.find_element(By.CSS_SELECTOR, f'[data-qa-title="{title}"] [data-qa="resume-update-button_actions"]')