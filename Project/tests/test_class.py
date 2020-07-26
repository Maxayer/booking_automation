import allure
from Project.pages.HomePage import HomePage
from Project.pages.HotelsPage import HotelsPage
import pytest


class TestClass:


    @allure.feature("booking.com tests")
    @allure.story("Check the number of children")
    @allure.severity("critical")
    @pytest.mark.parametrize("number_of_children", [2, 3, 4, 5])
    def test_first(self, driver, number_of_children):
        self.home_page = HomePage(driver)
        self.home_page.open_page()
        self.home_page.click_guests_dpd()

        self.home_page.increase_children_number(number_of_children)
        self.home_page.take_screenshot()
        assert self.home_page.get_number_of_children() == number_of_children, "Oops, you've missed someone"

    @allure.feature("booking.com tests")
    @allure.story("Check the hotels prices")
    @allure.severity("critical")
    def test_second(self, driver):
        try:
            self.home_page = HomePage(driver)
            self.home_page.open_page()
            self.home_page.click_first_hotel_bunner()

            self.hotels_page = HotelsPage(driver)
            assert self.hotels_page.is_at_page()
        finally:
            self.home_page.take_screenshot()

        try:
            self.number_of_hotels_on_page = len(self.hotels_page.get_hotels_on_page())
            assert self.number_of_hotels_on_page > 0, "There is no hotel on the page"
            assert len(
                self.hotels_page.get_show_price_buttons()) >= self.number_of_hotels_on_page, "Show price button doesn't seen on every hotel"

            self.hotels_page.click_on_hotel_by_index(0)
            self.hotels_page.click_on_next_month_day()
            self.hotels_page.click_on_search_btn()
            assert len(self.hotels_page.get_hotels_on_page()) == len(
                self.hotels_page.get_hotels_with_price()), "Some hotels are displayed without price"
        finally:
            self.hotels_page.take_screenshot()
