from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"/Users/tehnoezh/Documents/my_project"
    DRIVER_NAME = "chromdriver"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome( service=Service(BasePage.PATH + BasePage.DRIVER_NAME))

    def close(self):
        self.driver.close()
        