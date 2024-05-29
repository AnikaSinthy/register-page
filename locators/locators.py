from selenium.webdriver.common.by import By


class Locators():
    firstname = By.XPATH, '//input[@placeholder="First Name"]'
    lastname = By.XPATH, '//input[@placeholder="Last Name"]'
    Address = By.XPATH, "//textarea[@ng-model='Adress']"
    Emailaddress = By.XPATH, "//input[@type='email']"
    Phone = By.XPATH, "//input[@type='tel']"
    male = By.XPATH, "(//input[@name='radiooptions'])[1]"
    female = By.XPATH, "(//input[@name='radiooptions'])[2]"
    Cricket = By.ID, 'checkbox1'
    Movies = By.ID, 'checkbox2'
    Hockey = By.ID, 'checkbox3'
    languages = By.ID, 'msdd'
    English = By.XPATH, '//multi-select/div[2]/ul/li[8]'
    languages_text = By.XPATH, '//label[contains(text(),"Languages")]'
    skills = By.ID, 'Skills'
    # Country =
    SelectCountry = By.XPATH, '//span[@class="dropdown-wrapper"]/..'
    SearchCountry = By.XPATH, '//input[@class="select2-search__field"]'
    Year = By.XPATH, '//select[@id="yearbox"]'
    Month = By.XPATH, '//select[@ng-model="monthbox"]'
    Date = By.XPATH, '//select[@id="daybox"]'

    # DateofBirth =
    Password = By.XPATH, '//input[@id="firstpassword"]'
    ConfirmPassword = By.XPATH, '//input[@id="secondpassword"]'
    ImageUpload = By.XPATH, '//input[@id="imagesrc"]'
    Submit_Button = By.XPATH, "//button[@id='submitbtn']"
    imageUpload = By.ID, 'imagesrc'
