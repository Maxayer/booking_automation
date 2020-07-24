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
            self.driver = webdriver.Chrome(executable_path=self.exec_path)

        # is to be done
        if self.driver_name.lower() == "firefox":
            self.exec_path = Config.ROOT_DIR + "/resources/drivers/geckodriver.exe"
            self.driver = webdriver.Firefox(executable_path=self.exec_path)

        if self.driver_name.lower() == "opera":
            self.exec_path = Config.ROOT_DIR + "/resources/drivers/operadriver.exe"
            self.driver = webdriver.Opera(executable_path=self.exec_path)

        self.driver.implicitly_wait(5)
        return self.driver


