from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from Project.common.PageElement import PageElement


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_web_element(self, page_element):
        return self.driver.find_element(page_element.get_locator_type(), page_element.get_locator())

    def find_all_web_elements(self, page_element):
        return self.driver.find_elements(page_element.get_locator_type(), page_element.get_locator())

    def wait_to_be_clickable(self, page_element):
        self.wait.until(cond.element_to_be_clickable((page_element.get_locator_type(), page_element.get_locator())))

    def wait_to_be_present(self, page_element):
        self.wait.until(cond.presence_of_element_located((page_element.get_locator_type(), page_element.get_locator())))

    def click(self, page_element):
        if isinstance(page_element, PageElement):
            page_element = self.find_web_element(page_element)

        page_element.click()

    def enter_text(self, page_element, text):
        self.find_web_element(page_element).send_keys(text)

    def get_text(self, page_element):
        return self.find_web_element(page_element).text

    def get_attribute(self, page_element, attribute_name):
        return self.find_web_element(page_element).get_attribute(attribute_name)

    def take_screenshot(self):
        with allure.step("Take a screen"):
            allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)

    def is_at_page(self, title):
        raise NotEmplementedError("You should define is_at_page() method in all your pages")

