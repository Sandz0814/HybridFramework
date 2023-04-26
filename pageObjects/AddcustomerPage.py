import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from testCases import NameGenerator


class AddCustomer:
    # Add Customer page
    link_customer_module_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]"
    link_sub_customer_module_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]"
    btn_add_new_customer_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    text_box_email_xpath = "//input[@id='Email']"
    text_box_password_xpath = "//input[@id='Password']"
    text_box_firstname_xpath = "//input[@id='FirstName']"
    text_box_lastname_xpath = "//input[@id='LastName']"
    radio_male_xpath = "//input[@id='Gender_Male']"
    radio_female_xpath = "//input[@id='Gender_Female']"
    text_date_of_birth_xpath = "//input[@id='DateOfBirth']"
    text_company_name_xpath = "//input[@id='Company']"
    radio_tax_exempt_xpath = "//input[@id='IsTaxExempt']"
    select_box_newsletter_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]"
    select_box_newsletter_option_xpath = "//li[contains(text(),'Your store name')]"
    select_customer_roles_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"
    select_customer_roles_delete_xpath = '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]'
    select_customer_roles_option_xpath = "//li[contains(text(),'Forum Moderators')]"
    select_vendor_xpath = "//select[@id='VendorId']"
    select_vendor_option_xpath = "//option[contains(text(),'Vendor 1')]"
    radio_active_name = "Active"
    text_box_comment_xpath = "//textarea[@id='AdminComment']"
    btn_save_name = "save"

    def __init__(self, driver):
        self.driver = driver

    def link_customer_module(self):
        self.driver.find_element(By.XPATH, self.link_customer_module_xpath).click()

    def link_sub_customer_module(self):
        self.driver.find_element(By.XPATH, self.link_sub_customer_module_xpath).click()

    def btn_add_new_customer(self):
        self.driver.find_element(By.XPATH, self.btn_add_new_customer_xpath).click()

    def text_box_email(self, email):
        self.driver.find_element(By.XPATH, self.text_box_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_box_email_xpath).send_keys(email)

    def text_box_password(self, password):
        self.driver.find_element(By.XPATH, self.text_box_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_box_password_xpath).send_keys(password)

    def text_box_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.text_box_firstname_xpath).send_keys(firstname)

    def text_box_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.text_box_lastname_xpath).send_keys(lastname)

    def radio_male(self):
        self.driver.find_element(By.XPATH, self.radio_male_xpath).click()

    def radio_female(self):
        self.driver.find_element(By.XPATH, self.radio_female_xpath).click()

    def text_date_of_birth(self, dob):
        self.driver.find_element(By.XPATH, self.text_date_of_birth_xpath).send_keys(dob)

    def text_company_name(self, company):
        self.driver.find_element(By.XPATH, self.text_company_name_xpath).send_keys(company)

    def radio_tax_exempt(self):
        self.driver.find_element(By.XPATH, self.radio_tax_exempt_xpath).click()

    def select_box_newsletter(self):
        self.driver.find_element(By.XPATH, self.select_box_newsletter_xpath).click()

    def select_box_newsletter_option(self):
        self.driver.find_element(By.XPATH, self.select_box_newsletter_option_xpath).click()

    def select_customer_roles(self):
        self.driver.find_element(By.XPATH, self.select_customer_roles_xpath).click()

    def select_customer_roles_delete(self):
        self.driver.find_element(By.XPATH, self.select_customer_roles_delete_xpath).click()

    def select_customer_roles_option(self):
        self.driver.find_element(By.XPATH, self.select_customer_roles_option_xpath).click()

    def select_vendor(self):
        self.driver.find_element(By.XPATH, self.select_vendor_xpath).click()

    def select_vendor_option(self):
        self.driver.find_element(By.XPATH, self.select_vendor_option_xpath).click()

    def radio_active(self):
        self.driver.find_element(By.NAME, self.radio_active_name).click()

    def text_box_comment(self, msg):
        self.driver.find_element(By.XPATH, self.text_box_comment_xpath).send_keys(msg)

    def btn_save(self):
        self.driver.find_element(By.NAME, self.btn_save_name).click()













