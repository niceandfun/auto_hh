from selenium import webdriver


class IPage:
    def open(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError


class Page(IPage):
    def __init__(self, driver: webdriver):
        self.url = ''
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.close()

    def __enter__(self):
        self.driver.get(self.url)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
