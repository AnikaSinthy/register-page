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
        rp.select_gender_female()
        assert rp.assert_female_selected() == True
        rp.select_hobbies_hockey()
        assert rp.assert_hockey_selected() == True
        rp.enter_language()
        time.sleep(3)
        rp.select_android(DATA.value)
        time.sleep(2)
        rp.select_country(DATA.country_name)
        rp.select_year(DATA.year)
        rp.select_month()
        rp.select_date()
        rp.enter_password(DATA.VALID_PASSWORD)
        rp.enter_confirm_password(DATA.VALID_PASSWORD)
        rp.image_upload()
        rp.click_on_submit_button()

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
