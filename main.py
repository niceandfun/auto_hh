import os
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.resumes_page import ResumesPage
from dotenv import load_dotenv
from selenium import webdriver


def main():
    load_dotenv()

    driver = webdriver.Chrome()

    try:
        main_page = MainPage(driver)
        main_page.open()

        if main_page.is_unauthorized():
            login = os.getenv('LOGIN')
            password = os.getenv('PASSWORD')

            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(login, password)

        resumes_page = ResumesPage(driver)
        resumes_page.open()
        resumes_page.update_resume()

    except Exception as e:
        print(e)

    finally:
        driver.quit()


if __name__ == '__main__':
    main()
