import time

from selenium.webdriver.common.by import By

from locators.locators import Locators
from page.base_page import BasePage

class RegisterPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators

        self.firstname = By.XPATH, '//input[@placeholder="First Name"]'
        self.lastname = By.XPATH, '//input[@placeholder="Last Name"]'
        self.Address = By.XPATH, "//textarea[@ng-model='Adress']"
        self.Emailaddress = By.XPATH, "//input[@type='email']"
        self.Phone = By.XPATH, "//input[@type='tel']"
        # self.Gender =
        # self.Hobbies =
        self.Languages = By.XPATH, "//div[@class='ui-autocomplete-multiselect ui-state-default ui-widget']"
        # self.Skills =
        # self.Country =
        # self.SelectCountry =
        # self.DateofBirth =
        self.Password = By.XPATH, '//input[@id="firstpassword"]'
        self.ConfirmPassword = By.XPATH, '//input[@id="secondpassword"]'
        self.Submit_Button = By.XPATH, "//button[@id='submitbtn']"

    def enter_firstname(self, firstname):
        #self.driver.find_element(*self.firstname).send_keys(firstname)
        self.enter_at(self.firstname, firstname)

    def enter_lastname(self, lastname):
        #self.driver.find_element(*self.lastname).send_keys(lastname)
        self.enter_at(self.lastname, lastname)

    def enter_address(self, address):
        #self.driver.find_element(*self.Address).send_keys(address)
        self.enter_at(self.Address, address)

    def enter_email(self, email):
        #self.driver.find_element(*self.Emailaddress).send_keys(email)
        self.enter_at(self.Emailaddress, email)

    def enter_phone(self, phone):
        #self.driver.find_element(*self.Phone).send_keys(phone)
        self.enter_at(self.Phone, phone)

    def enter_language(self, language):
        #self.driver.find_element(*self.Languages).send_keys(language)
        self.enter_at(self.Languages, language)


    def enter_password(self, password):
        #self.driver.find_element(*self.Password).send_keys(password)
        self.enter_at(self.Password, password)


    def enter_confirm_password(self, password):
        #self.driver.find_element(*self.Password).send_keys(password)
        self.enter_at(self.Password, password)

    def click_on_submit_button(self):
        #self.driver.find_ele(*self.Submit_Button).click()
        self.click_element(self.Submit_Button)
        time.sleep(5)
