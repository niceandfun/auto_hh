from selenium.webdriver.chrome import webdriver

from pages.page import Page


class ResumesPage(Page):
    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)
        self.url = 'https://hh.ru/applicant/resumes'

    def update_resume(self, title):
        pass