from selenium import webdriver


class IBasePage:
    def open(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError


class BasePage(IBasePage):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
