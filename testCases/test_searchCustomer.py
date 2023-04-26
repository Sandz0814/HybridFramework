import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Loginpage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customloggers import LogGen
from utilities import ExcelUtils
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
import pytest

class Test_seachCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    testlog = LogGen.loggen()

    @pytest.mark.regression
    def test_search_customer_by_name(self, setup):

        self.testlog.info("**** Verifying login test ****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.testlog.info("**** Login successfully ****")

        self.testlog.info("**** Staring Search customer test ****")

        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.link_customer_module()
        self.searchcust.link_sub_customer_module()
        time.sleep(5)
        self.testlog.info("**** Providing customer information to search ****")
        self.driver.implicitly_wait(5)
        # self.searchcust.search_by_email("admin@yourStore.com")
        self.searchcust.search_by_firstname("John")
        self.searchcust.search_by_lastname("Smith")

        self.searchcust.search_button()
        time.sleep(5)

        searched = self.driver.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr/td[3]').is_displayed()
        if searched == True:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searched_name_scr.png")
            self.testlog.error("*** Search customer Failed ***")
            assert True == False
            time.sleep(5)
            self.testlog.info("*** Ending of Searched Page Test ***")
            self.driver.close()

    @pytest.mark.sanity
    def test_search_customer_by_email(self, setup):

        self.testlog.info("**** Verifying login test ****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.testlog.info("**** Login successfully ****")

        self.testlog.info("**** Staring Search customer test ****")

        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.link_customer_module()
        self.searchcust.link_sub_customer_module()
        time.sleep(5)
        self.testlog.info("**** Providing customer information to search ****")

        self.driver.implicitly_wait(5)
        self.searchcust.search_by_email("admin@yourStore.com")
        # self.searchcust.search_by_firstname("John")
        # self.searchcust.search_by_lastname("Smith")

        self.searchcust.search_button()
        time.sleep(5)

        searched = self.driver.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr[1]/td[2]').is_displayed()
        if searched == True:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searched_email_scr.png")
            self.testlog.error("*** Search customer Failed ***")
            assert True == False
            time.sleep(10)
            self.testlog.info("*** Ending of Searched Page Test ***")
            self.driver.close()





