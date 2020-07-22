from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Project.common.PageElement import PageElement
from Project.pages.BasePage import BasePage
from Project.common.helper import Helper


class HotelsPage(BasePage):
    hotels_on_page = PageElement("The list of hotels on the page", By.CSS_SELECTOR,
                     "div.sr_property_block_main_row", False)

    show_price_button = PageElement("Button to reveal the hotel prices",
                        By.XPATH, "//span[@class='bui-button__text']", False)

    fifteen_day_of_next_month_calendar_table = PageElement("Fifteenth day of next month",By.CSS_SELECTOR,
                                               f"td[data-date='2020-{Helper.get_next_month()}-15']", False)

    search_btn = PageElement("Search button", By.XPATH,"//button[@class='sb-searchbox__button ']", False)

    hotels_with_price = PageElement("Hotels with the displayed price", By.XPATH,
                        "//div[@class='bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper']",
                        False)

    def get_hotels_on_page(self):
        self.wait_to_be_present(self.hotels_on_page)
        return self.find_all_web_elements(self.hotels_on_page)

    def get_show_price_buttons(self):
        self.wait_to_be_present(self.show_price_button)
        return self.find_all_web_elements(self.show_price_button)

    def click_on_hotel_by_index(self, index):
        self.find_all_web_elements(self.show_price_button)[index].find_element(By.XPATH, ".").click()

    def click_on_next_month_day(self):
        self.wait_to_be_clickable(self.fifteen_day_of_next_month_calendar_table)
        self.click(self.fifteen_day_of_next_month_calendar_table)

    def click_on_search_btn(self):
        self.wait_to_be_clickable(self.search_btn)
        self.click(self.search_btn)

    def get_hotels_with_price(self):
        self.wait_to_be_present(self.hotels_with_price)
        return self.find_all_web_elements(self.hotels_with_price)