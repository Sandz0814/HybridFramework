import time
import pytest
from selenium import webdriver
import allure
import logging
from pageObjects.Loginpage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customloggers import LogGen
from utilities import ExcelUtils
from testCases import NameGenerator


class TestLogin_DDT_01:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/user and pass.xlsx"

    testlog = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.testlog.info("**** ddt test login ****")
        self.testlog.info("**** Verifying login test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in the Excel:", self.rows+1)

        list_status = []   # empty list variables

        for r in range(2, self.rows+1):
            self.username = ExcelUtils.readData(self.path, "Sheet1", r, 1)
            self.password = ExcelUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = ExcelUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.testlog.info("**passed**")
                    self.lp.clicklogout()
                    list_status.append("Pass")
                elif self.exp == "fail":
                    self.testlog.info("**failed**")
                    self.lp.clicklogout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Passed":
                    self.testlog.info("*** failed ***")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.testlog.info("*** Passed ***")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.testlog.info("***Login DDT is Passed***")
            self.driver.close()
            assert True
        else:
            self.testlog.info("***Login DDT is Failed***")
            self.driver.close()
            assert False

        self.testlog.info("*** End of Login DDT test ***")
        self.testlog.info("*** Completed TestLogin_DDT_01 ***")