import time
import unittest
from selenium import webdriver


class Base_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://demo.automationtesting.in/Register.html')
        self.driver.maximize_window()
        time.sleep(5)
        print("I am running from setUp method")


def tearDown(self):
    self.driver.close()
    print("I am running from tearDown method")
