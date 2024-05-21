class Base_Test(unittest.TestCase):

     def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.demoblaze.com/index.html')
        self.driver.maximize_window()
        time.sleep(5)
        print("I am running from setUp method")

    def tearDown(self):
        self.driver.close()
        print("I am running from tearDown method")




