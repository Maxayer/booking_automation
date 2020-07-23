from selenium import webdriver
from Project.config import Config


class DriverFactory:
    def __init__(self, driver_name):
        if type(driver_name) is str:
            self.driver_name = driver_name
            self.exec_path = ""

    def get_driver(self):
        if self.driver_name.lower() == "chrome":
            self.exec_path = Config.ROOT_DIR + "/resources/drivers/chromedriver.exe"
            driver = webdriver.Chrome(self.exec_path)
            driver.implicitly_wait(5)
            return driver

        # is to be done
        if self.driver_name.lower() == "firefox":
            self.exec_path = Config.ROOT_DIR + "/resources/drivers/geckodriver.exe"
            driver = webdriver.Firefox(self.exec_path)
            driver.implicitly_wait(5)
            return driver



