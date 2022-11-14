from pages.page import IPage


class ResumesPage(IPage):
    def __init__(self, driver):
        self.url = 'https://hh.ru/applicant/resumes'
        self.driver = driver

    def open(self):
        self.driver.get(self.url)
