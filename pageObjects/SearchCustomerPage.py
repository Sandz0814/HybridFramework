from selenium.webdriver.common.by import By
from pageObjects.AddcustomerPage import AddCustomer


class SearchCustomer:
    link_customer_module_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]"
    link_sub_customer_module_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]"
    btn_add_new_customer_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    search_by_email_xpath = "//input[@id='SearchEmail']"
    search_by_firstname_xpath = "//input[@id='SearchFirstName']"
    search_by_lastname_xpath = "//input[@id='SearchLastName']"
    search_by_dob_xpath = "//select[@id='SearchMonthOfBirth']"
    search_by_dob_month_xpath = '//*[@id="SearchMonthOfBirth"]/option[9]'
    search_by_dob_day_xpath = "//select[@id='SearchDayOfBirth']"
    search_by_dob_day_option_xpath = '//*[@id="SearchDayOfBirth"]/option[9]'
    search_by_regs_date_from_xpath = "//input[@id='SearchRegistrationDateFrom']"
    search_by_regs_date_to_xpath = "//input[@id='SearchRegistrationDateTo']"
    search_by_last_activity_date_from_xpath = "//input[@id='SearchLastActivityFrom']"
    search_by_last_activity_date_to_xpath = "//input[@id='SearchLastActivityTo']"
    search_company_by_name_xpath = "//input[@id='SearchCompany']"
    search_by_ip_address_xpath = "//input[@id='SearchIpAddress']"
    search_by_customer_roles_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[5]/div[2]/div[1]/div[1]"
    search_by_customer_roles_option_xpath = "//option[contains(text(),'Forum Moderators')]"
    search_button_xpath = "//button[@id='search-customers']"

    def __init__(self, driver):
        self.driver = driver
    def link_customer_module(self):
        self.driver.find_element(By.XPATH, self.link_customer_module_xpath).click()

    def link_sub_customer_module(self):
        self.driver.find_element(By.XPATH, self.link_sub_customer_module_xpath).click()

    def btn_add_new_customer(self):
        self.driver.find_element(By.XPATH, self.btn_add_new_customer_xpath).click()

    def search_by_email(self, email):
        self.driver.find_element(By.XPATH, self.search_by_email_xpath).send_keys(email)

    def search_by_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.search_by_firstname_xpath).send_keys(firstname)

    def search_by_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.search_by_lastname_xpath).send_keys(lastname)

    def search_by_dob(self, dob):
        self.driver.find_element(By.XPATH, self.search_by_dob_xpath).click()

    def search_by_dob_month(self):
        self.driver.find_element(By.XPATH, self.search_by_dob_month_xpath).click()

    def search_by_dob_day(self):
        self.driver.find_element(By.XPATH, self.search_by_dob_day_xpath).click()

    def search_by_dob_day_option(self):
        self.driver.find_element(By.XPATH, self.search_by_dob_day_option_xpath).click()

    def search_by_regs_date_from(self, regs_date_from):
        self.driver.find_element(By.XPATH, self.search_by_regs_date_from_xpath).send_keys(regs_date_from)

    def search_by_regs_date_to(self, regs_date_to):
        self.driver.find_element(By.XPATH, self.search_by_regs_date_to_xpath).send_keys(regs_date_to)

    def search_by_last_activity_date_from(self, activity_from):
        self.driver.find_element(By.XPATH, self.search_by_last_activity_date_from_xpath).send_keys(activity_from)

    def search_by_last_activity_date_to(self, activity_to):
        self.driver.find_element(By.XPATH, self.search_by_last_activity_date_to_xpath).send_keys(activity_to)

    def search_company_by_name(self, company_name):
        self.driver.find_element(By.XPATH, self.search_company_by_name_xpath).send_keys(company_name)

    def search_by_ip_address(self, ip):
        self.driver.find_element(By.XPATH, self.search_by_ip_address_xpath).send_keys(ip)

    def search_by_customer_roles(self):
        self.driver.find_element(By.XPATH, self.search_by_customer_roles_xpath).click()

    def search_by_customer_roles_option(self):
        self.driver.find_element(By.XPATH, self.search_by_customer_roles_option_xpath).click()

    def search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()











