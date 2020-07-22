from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Project.pages.BasePage import BasePage
from Project.common.PageElement import PageElement


class HomePage(BasePage):

    url = "https://www.booking.com/"

    flight_btn = PageElement("Flight Button", By.XPATH, "//a[@class='xpb__link'][2]", False)

    guests_dpd = PageElement("Button for ordering beds", By.CSS_SELECTOR, "#xp__guests__toggle", False)

    increase_children_number_btn = PageElement ("Increase children number button",By.CSS_SELECTOR,
                                   "button[aria-label='Детей: увеличить количество']", False)

    number_of_children = PageElement("Number of children on the drop down menu for ordering beds",
                         By.CSS_SELECTOR, "#group_children", False)

    first_hotel_bunner = PageElement("The first hotel bunner on the home page",
                         By.CSS_SELECTOR, "div[data-no-follow-link='1']", False)

    def open_page(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def click_flight_btn(self):
        self.wait_to_be_clickable(self.flight_btn)
        self.click(self.flight_btn)

    def click_guests_dpd(self):
        self.wait_to_be_clickable(self.guests_dpd)
        self.click(self.guests_dpd)

    def increase_children_number(self, number):
        self.wait_to_be_clickable(self.increase_children_number_btn)
        for i in range(0, number):
            self.click(self.increase_children_number_btn)

    def get_number_of_children(self):
        self.wait_to_be_present(self.number_of_children)
        return int(self.get_attribute(self.number_of_children, "value"))

    def click_first_hotel_bunner(self):
        self.wait_to_be_clickable(self.first_hotel_bunner)
        self.click(self.first_hotel_bunner)