class RegisterTest(Base_Test):

    def test_valid_register(self):
        rp = RegisterPage(self.driver)
        rp.enter_fullname(DATA.VALID_FIRSTNAME)
        rp.enter_fullname(DATA.VALID_LASTNAME)
        rp.enter_address(DATA.VALID_ADDRESS)
        rp.enter_email(DATA.VALID_EMAIL)
        rp.enter_phone(DATA.VALID_PHONE)
        rp.enter_language(DATA.VALID_LANGUAGE)
        rp.enter_password(DATA.VALID_PASSWORD)
        rp.enter_confirm_password(DATA.VALID_PASSWORD)
        rp.click_on_submit_Button()

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
