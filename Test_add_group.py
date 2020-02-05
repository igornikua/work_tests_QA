# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        self.open_home_page(driver)
        self.Login(driver, username="admin", password="secret")
        self.open_groups_page(driver)
        self.init_group_creation(driver)
        self.fill_group_firm(driver, Group(name="gjnkulii.,gnbfbf", header="wsfegtjhykilill", footer="sfvfhyukili"))
        self.submit_group_creation(driver)
        self.return_to_groups_pade(driver)
        self.Logout(driver)

    def test_untitled_empty_test_case(self):
        # git check
        driver = self.driver
        self.open_home_page(driver)
        self.Login(driver, username="admin", password="secret")
        self.open_groups_page(driver)
        self.init_group_creation(driver)
        self.fill_group_firm(driver, Group(name="", header="", footer=""))
        self.submit_group_creation(driver)
        self.return_to_groups_pade(driver)
        self.Logout(driver)

    def Logout(self, driver):
        # Logout
        driver.find_element_by_link_text("Logout").click()

    def return_to_groups_pade(self, driver):
        # return to groups pade
        driver.find_element_by_link_text("group page").click()

    def submit_group_creation(self, driver):
        # submit group creation
        driver.find_element_by_name("submit").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Groups'])[1]/following::div[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Groups'])[1]/following::div[1]").click()

    def fill_group_firm(self, driver, group):
        # fill group firm
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)

    def init_group_creation(self, driver):
        # init group creation
        driver.find_element_by_name("new").click()

    def open_groups_page(self, driver):
        # open groups page
        driver.find_element_by_link_text("groups").click()

    def Login(self, driver, username, password):
        # login
        driver.find_element_by_xpath("//*/text()[normalize-space(.)='']/parent::*").click()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_id("LoginForm").click()
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        # open home page
        driver.get("http://localhost/addressbook/group.php")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
