import os

from selenium import webdriver

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.resumes_page import ResumesPage
from dotenv import load_dotenv


def main():
    load_dotenv()

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    try:
        main_page = MainPage(driver)
        main_page.open()

        if main_page.is_unauthorized():
            login = os.getenv('LOGIN')
            password = os.getenv('PASSWORD')

            with LoginPage(driver) as login_page:
                login_page.login(login, password)

        with ResumesPage(driver) as resumes_page:
            resumes_page.update_resume('developer')

    finally:
        driver.quit()


if __name__ == '__main__':
    main()
