from selenium import webdriver
from pages.main_page import MainPage
from pages.resumes_page import ResumesPage


def main():
    driver = webdriver.Chrome()

    main_page = MainPage(driver)
    main_page.authorize()

    resumes_page = ResumesPage(driver)
    resumes_page.update_resume('developer')


if __name__ == '__main__':
    main()
