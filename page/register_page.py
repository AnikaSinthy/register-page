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

    def select_hobbies(self):
        self.click_element(self.locator.cricket)
        time.sleep(1)
        self.click_element(self.locator.movies)

    def enter_language(self):
        self.click_element(self.locator.languages)
        time.sleep(1)
        self.click_element(self.locator.arabic)
        time.sleep(1)
        self.click_element(self.locator.languageText)

    def select_android(self):
        # self.select_by_value(self.locator.skills, "Android")
        # self.select_by_text(self.locator.skills, "Adobe Photoshop")
        self.select_by_index(self.locator.skills, 8)

    def select_country(self, country_name):
        self.click_element(self.locator.selectCountry)
        time.sleep(1)
        self.enter_at(self.locator.searchTextBox, country_name)
        time.sleep(1)
        self.enter_at(self.locator.searchTextBox, Keys.ENTER)

    def enter_password(self, password):
        # self.driver.find_element(*self.Password).send_keys(password)
        self.enter_at(self.Password, password)

    def enter_confirm_password(self, password):
        # self.driver.find_element(*self.Password).send_keys(password)
        self.enter_at(self.Password, password)

    def click_on_submit_button(self):
        # self.driver.find_ele(*self.Submit_Button).click()
        self.click_element(self.Submit_Button)
        time.sleep(5)
