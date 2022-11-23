from selenium import webdriver


class IBasePage:
    pass

    def open(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


class BasePage(IBasePage):
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.switch_to.new_window('tab')
        self.driver.get(self.url)

    def close(self):
        self.driver.close()
