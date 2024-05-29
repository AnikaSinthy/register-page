import time

from test.base_test import Base_Test
from page.register_page import RegisterPage
from data.data import TestData as DATA


class RegisterTest(Base_Test):

    def test_valid_register(self):
        rp = RegisterPage(self.driver)
        rp.enter_firstname(DATA.VALID_FIRSTNAME)
        rp.enter_lastname(DATA.VALID_LASTNAME)
        rp.enter_address(DATA.VALID_ADDRESS)
        rp.enter_email(DATA.VALID_EMAIL)
        rp.enter_phone(DATA.VALID_PHONE)
        time.sleep(2)
        rp.select_gender_male()
        time.sleep(1)
        assert rp.assert_male_selected() == True
        rp.select_hobbies()
        time.sleep(2)
        rp.enter_language()
        time.sleep(2)
        rp.select_android()
        time.sleep(2)
        rp.select_country(country_name="Bangladesh")
        time.sleep(2)
        rp.image_upload()
        time.sleep(5)
        # rp.enter_password(DATA.VALID_PASSWORD)
        # rp.enter_confirm_password(DATA.VALID_PASSWORD)
        # time.sleep(5)
        # rp.click_on_submit_button()

        print("I am running from test_invalid_login method")

    def test_invalid_register(self):
        rp = RegisterPage(self.driver)
        rp.enter_fullname(DATA.VALID_FIRSTNAME)
        rp.enter_fullname(DATA.INVALID_LASTNAME)
        rp.enter_address(DATA.VALID_ADDRESS)
        rp.enter_email(DATA.INVALID_EMAIL)
        rp.enter_phone(DATA.VALID_PHONE)
        rp.select_gender_male()
        rp.select_hobbies()
        rp.enter_language()
        rp.enter_password(DATA.INVALID_PASSWORD)
        rp.enter_confirm_password(DATA.VALID_PASSWORD)
        rp.click_on_submit_button()

        print("I am running from test_invalid_login method")
