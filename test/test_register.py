import time

from test.base_test import Base_Test
from page.register_page import Register_Page
from data.data import TestData as DATA


class RegisterTest(Base_Test):

    def test_valid_register(self):
        rp = Register_Page(self.driver)
        rp.enter_firstname(DATA.VALID_FIRSTNAME)
        rp.enter_lastname(DATA.VALID_LASTNAME)
        time.sleep(5)
        rp.enter_address(DATA.VALID_ADDRESS)
        rp.enter_email(DATA.VALID_EMAIL)
        rp.enter_phone(DATA.VALID_PHONE)
        rp.enter_language(DATA.VALID_LANGUAGE)
        rp.enter_password(DATA.VALID_PASSWORD)
        rp.enter_confirm_password(DATA.VALID_PASSWORD)
        rp.click_on_submit_button()

        print("I am running from test_invalid_login method")

    def test_invalid_register(self):
        rp = RegisterPage(self.driver)
        rp.enter_fullname(DATA.VALID_FIRSTNAME)
        rp.enter_fullname(DATA.INVALID_LASTNAME)
        rp.enter_address(DATA.VALID_ADDRESS)
        rp.enter_email(DATA.INVALID_EMAIL)
        rp.enter_phone(DATA.VALID_PHONE)
        rp.enter_language(DATA.VALID_LANGUAGE)
        rp.enter_password(DATA.INVALID_PASSWORD)
        rp.enter_confirm_password(DATA.VALID_PASSWORD)
        rp.click_on_submit_Button()

        print("I am running from test_invalid_login method")
