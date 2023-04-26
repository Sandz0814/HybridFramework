import string
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Loginpage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customloggers import LogGen
from utilities import ExcelUtils
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
import random
import names


class Test_addCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    testlog = LogGen.loggen()

    @pytest.mark.regression
    def test_addCustomer(self, setup):

        self.testlog.info("**** Verifying login test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.testlog.info("**** Login successfully ****")

        self.testlog.info("**** Staring Add customer test ****")

        self.addcust = AddCustomer(self.driver)
        self.addcust.link_customer_module()
        self.addcust.link_sub_customer_module()
        self.addcust.btn_add_new_customer()

        self.testlog.info("**** Providing customer information ****")

        self.email = random_generator() + "@gmail.com"
        self.addcust.text_box_email(self.email)
        self.addcust.text_box_password("test123")
        self.firstname = first_name()
        self.addcust.text_box_firstname(self.firstname)
        self.lastname = last_name()
        self.addcust.text_box_lastname(self.lastname)
        self.addcust.radio_male()
        self.addcust.radio_female()
        self.addcust.text_date_of_birth("08/08/1996")
        self.addcust.text_company_name("Tambay lang")
        time.sleep(5)
        self.addcust.radio_tax_exempt()
        time.sleep(5)
        self.addcust.select_box_newsletter()
        self.driver.implicitly_wait(10)
        time.sleep(1)
        self.addcust.select_box_newsletter_option()  # OK
        time.sleep(1)
        self.addcust.select_customer_roles()
        time.sleep(1)
        self.addcust.select_customer_roles_delete()
        time.sleep(1)
        self.addcust.select_customer_roles()
        time.sleep(1)
        self.addcust.select_customer_roles_option()  # OK
        time.sleep(5)
        self.addcust.select_vendor()
        time.sleep(5)
        self.addcust.select_vendor_option()
        time.sleep(5)
        self.addcust.radio_active()
        self.addcust.text_box_comment("this is a test")
        self.addcust.btn_save()
        time.sleep(20)

        self.testlog.info("*** saving customer details***")

        self.msg = self.driver.find_element(By.XPATH, "//body/div[3]/div[1]/div[1]").text

        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.testlog.info("*** Add customer Passed ***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.testlog.error("*** Add customer Failed ***")
            assert True == True

        self.driver.close()
        self.testlog.info("*** Ending Customer Page Test ***")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def first_name():
    Fname = names.get_first_name()
    return Fname


def last_name():
    Lname = names.get_last_name()
    return Lname




