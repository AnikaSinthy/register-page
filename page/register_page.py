import os.path
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from locators.locators import Locators
from page.base_page import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators

    def enter_firstname(self, firstname):
        # self.driver.find_element(*self.firstname).send_keys(firstname)
        self.enter_at(self.locator.firstname, firstname)

    def enter_lastname(self, lastname):
        # self.driver.find_element(*self.lastname).send_keys(lastname)
        self.enter_at(self.locator.lastname, lastname)

    def enter_address(self, address):
        # self.driver.find_element(*self.Address).send_keys(address)
        self.enter_at(self.locator.Address, address)

    def enter_email(self, email):
        # self.driver.find_element(*self.Emailaddress).send_keys(email)
        self.enter_at(self.locator.Emailaddress, email)

    def enter_phone(self, phone):
        # self.driver.find_element(*self.Phone).send_keys(phone)
        self.enter_at(self.locator.Phone, phone)

    def select_gender_male(self):
        self.click_element(self.locator.male)

    def assert_male_selected(self):
        value = self.is_selected(self.locator.male)
        print(value)
        return value

    def select_gender_female(self):
        self.click_element(self.locator.female)

    def assert_female_selected(self):
        value = self.is_selected(self.locator.female)
        print(value)
        return value

    def select_hobbies_cricket(self):
        self.click_element(self.locator.Cricket)

    def assert_cricket_selected(self):
        value = self.is_selected(self.locator.Cricket)
        print(value)
        return value

    def select_hobbies_movies(self):
        self.click_element(self.locator.Movies)

    def assert_movies_selected(self):
        value = self.is_selected(self.locator.Movies)
        print(value)
        return (value)

    def select_hobbies_hockey(self):
        self.click_element(self.locator.Hockey)

    def assert_hockey_selected(self):
        value = self.is_selected(self.locator.Hockey)
        print(value)
        return value

    def select_hobbies(self):
        self.click_element(self.locator.Movies)
        self.click_element(self.locator.Hockey)

    def assert_hobbies_selected(self):
        value_1 = self.is_selected(self.locator.Movies)
        value_2 = self.is_selected(self.locator.Hockey)
        assert value_1 == True
        assert value_2 == True

    def enter_language(self):
        # self.driver.find_element(*self.Languages).send_keys(language)
        self.click_element(self.locator.languages)
        self.click_element(self.locator.English)
        self.click_element(self.locator.languages_text)

    def select_android(self):
        self.selected_by_value(self.locator.skills, value)

    def select_country(self):
        self.click_element(self.locator.SelectCountry)
        self.enter_at(self.locator.SearchCountry, country_name)
        self.enter_at(self.locator.SearchCountry, Keys.ENTER)

    def select_year(self, year):
        self.selected_by_value(self.locator.Year, year)

    def select_month(self):
        self.selected_by_text(self.locator.Month, value="November")

    def select_date(self):
        self.selected_by_value(self.locator.Date, value="21")

    def enter_password(self, password):
        # self.driver.find_element(*self.Password).send_keys(password)
        self.enter_at(self.locator.Password, password)

    def enter_confirm_password(self, password):
        # self.driver.find_element(*self.Password).send_keys(password)
        self.enter_at(self.locator.Password, password)

    def image_upload(self):
        directory = os.path.abspath(
            os.path.join(os.path.dirname(__file__),"..","image/Screenshot 2024-04-27 231325.png"))
        self.enter_at(self.locator.ImageUpload,directory)

    def click_on_submit_button(self):
        # self.driver.find_ele(*self.Submit_Button).click()
        self.click_element(self.locator.Submit_Button)
        time.sleep(5)
