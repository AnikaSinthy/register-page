import time

from selenium.webdriver.common.by import By


class Register_Page():

    def __init__(self, driver):
        self.driver = driver

        self.firstname = By.XPATH, '//input[@placeholder="First Name"]'
        self.lastname = By.XPATH, '//input[@placeholder="Last Name"]'
        self.Address = By.NAME, "Address"
        self.Emailaddress = By.NAME, "email"
        self.Phone = By.NAME, "phone"
        # self.Gender =
        # self.Hobbies =
        self.Languages = By.NAME, "languages"
        # self.Skills =
        # self.Country =
        # self.SelectCountry =
        # self.DateofBirth =
        self.Password = By.NAME, "Password"
        self.ConfirmPassword = By.NAME, "Password"
        self.Submit_Button = By.XPATH, "//button[@id='submitbtn']"

    def enter_firstname(self, firstname):
        self.driver.find_element(*self.firstname).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(*self.lastname).send_keys(lastname)

    def enter_address(self, address):
        self.driver.find_element(*self.Address).send_keys(address)

    def enter_email(self, email):
        self.driver.find_element(*self.Emailaddress).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(*self.Phone).send_keys(phone)

    def enter_language(self, language):
        self.driver.find_element(*self.Languages).send_keys(language)

    def enter_password(self, password):
        self.driver.find_element(*self.Password).send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.find_element(*self.Password).send_keys(password)

    def click_on_submit_button(self):
        self.driver.find_element(*self.Submit_Button).click()
        time.sleep(5)
