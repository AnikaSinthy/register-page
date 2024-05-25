from selenium.webdriver.common.by import By


class Locators():
    firstname = By.XPATH, '//input[@placeholder="First Name"]'
    lastname = By.XPATH, '//input[@placeholder="Last Name"]'
    Address = By.XPATH, "//textarea[@ng-model='Adress']"
    Emailaddress = By.XPATH, "//input[@type='email']"
    Phone = By.XPATH, "//input[@type='tel']"
    male = By.XPATH, '(//input[@name="radiooptions"])[1]'
    female = By.XPATH, '(//input[@name="radiooptions"])[2]'
    # Hobbies
    cricket = By.ID, 'checkbox1'
    movies = By.ID, 'checkbox2'
    hockey = By.ID, 'checkbox3'
    languages = By.ID, "msdd"
    arabic = By.XPATH, "//multi-select/div[2]/ul/li[1]"
    languageText = By.XPATH, '//label[contains(text(), "Languages")]'
    skills = By.ID, 'Skills'
    # Country =
    selectCountry = By.XPATH, '//span[@id="select2-country-container"]/..'
    searchTextBox = By.XPATH, '//input[@class="select2-search__field"]'
    # DateofBirth =
    Password = By.XPATH, '//input[@id="firstpassword"]'
    ConfirmPassword = By.XPATH, '//input[@id="secondpassword"]'
    Submit_Button = By.XPATH, "//button[@id='submitbtn']"
    imageUpload = By.ID, 'imagesrc'
