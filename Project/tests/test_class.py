import allure
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from allure_commons.types import AttachmentType
from Project.common.factories.driver_factory import DriverFactory
from Project.pages.HomePage import HomePage
from Project.pages.HotelsPage import HotelsPage


class TestClass:
    def setup(self):
        self.driver_factory = DriverFactory("google")
        self.driver = self.driver_factory.get_driver()
        self.home_page = HomePage(self.driver)

    def teardown(self):
        time.sleep(10)
        self.driver.quit()

    @allure.feature("booking.com tests")
    @allure.story("Check the number of children")
    @allure.severity("critical")
    def test_first(self):
        self.home_page.open_page()
        self.home_page.click_guests_dpd()

        self.number_of_children = 3
        self.home_page.increase_children_number(self.number_of_children)
        self.home_page.take_screenshot()
        assert self.home_page.get_number_of_children() == self.number_of_children, "Oops, you've missed someone"

    @allure.feature("booking.com tests")
    @allure.story("Check the hotels prices")
    @allure.severity("critical")
    def test_second(self):
        self.home_page.open_page()
        self.home_page.click_first_hotel_bunner()

        self.hotels_page = HotelsPage(self.driver)

        self.number_of_hotels_on_page = len(self.hotels_page.get_hotels_on_page())
        assert self.number_of_hotels_on_page > 0, "There is no hotel on the page"
        assert len(self.hotels_page.get_show_price_buttons()) >= self.number_of_hotels_on_page, "Show price button doesn't seen on every hotel"

        self.hotels_page.click_on_hotel_by_index(0)
        self.hotels_page.click_on_next_month_day()
        self.hotels_page.click_on_search_btn()
        assert len(self.hotels_page.get_hotels_on_page()) == len(self.hotels_page.get_hotels_with_price()), "Some hotels are displayed without price"
        self.home_page.take_screenshot()
