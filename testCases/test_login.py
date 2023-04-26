import time
import pytest
from selenium import webdriver
import allure
import logging
from pageObjects.Loginpage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customloggers import LogGen


class TestLogin:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    testlog = LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.testlog.info("**** Test_001_Login ****")
        self.testlog.info("**** Verifying Home Page Title ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.testlog.info("**** Home Page Title page is passed ****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.testlog.info("**** Home Page Title page is failed ****")
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.testlog.info("**** Verifying login test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.testlog.info("**** Home Page Title page is passed ****")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.testlog.info("**** Home Page Title page is failed ****")
            assert False



