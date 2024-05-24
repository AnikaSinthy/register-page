from selenium.webdriver.common.by import By


class Locators():
    firstname = By.XPATH, '//input[@placeholder="First Name"]'
    lastname = By.XPATH, '//input[@placeholder="Last Name"]'
    Address = By.XPATH, "//textarea[@ng-model='Adress']"
    Emailaddress = By.XPATH, "//input[@type='email']"
    Phone = By.XPATH, "//input[@type='tel']"
    # Gender =
    # Hobbies =
    Languages = By.XPATH, "//div[@class='ui-autocomplete-multiselect ui-state-default ui-widget']"
    # Skills =
    # Country =
    # SelectCountry =
    # DateofBirth =
    Password = By.XPATH, '//input[@id="firstpassword"]'
    ConfirmPassword = By.XPATH, '//input[@id="secondpassword"]'
    Submit_Button = By.XPATH, "//button[@id='submitbtn']"
