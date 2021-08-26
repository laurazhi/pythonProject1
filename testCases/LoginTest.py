import unittest
import time
import HTMLTestRunner
from selenium import webdriver
import sys
sys.path.append("C://Users/laura/PycharmProjects/pythonProject/pythonProject1")
from pageObjects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    username = "codechallenge"
    password = "Password123"
    baseURL = "https://clarity.dexcom.com"
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\laura\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp=LoginPage(self.driver)
        lp.clickHomeUser()
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dexcom CLARITY", self.driver.title, "webpage title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(testRunner=HTMLTestRunner.__version__(output='..\\reports'))






