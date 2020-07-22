from selenium import webdriver
from Project.config import Config


class DriverFactory:
    def __init__(self, driver_name):
        if type(driver_name) is str:
            self.driver_name = driver_name

    def get_driver(self):
        if self.driver_name.lower() == "google":
            exec_path = Config.ROOT_DIR + "/resources/drivers/chromedriver.exe"
            driver = webdriver.Chrome(exec_path)
            driver.implicitly_wait(5)
            return driver

        # is to be done
        if self.driver_name.lower() == "firefox":
            pass

