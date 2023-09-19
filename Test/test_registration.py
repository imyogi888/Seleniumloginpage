import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Testdata.testpagedata import testpagedata
from pageobject.HomePage import homepage
from pageobject.Registerpage import registerpage
from utilities.baseclass import Baseclass


class Testregistration(Baseclass):
    def test_registration(self,getttdata):
        home= homepage(self.driver)
        home.forget().click()
        register= registerpage(self.driver)
        register.registerlink().click()
        register.firstname().send_keys(getttdata["firstname"])
        register.lastname().send_keys(getttdata["lastname"])
        register.emailid().send_keys(getttdata["emailid"])
        register.mobilenumber().send_keys(getttdata["mobilenumber"])
        dropdown = Select(register.dropdown())
        dropdown.select_by_visible_text("Engineer")
        register.gender().click()
        register.userpassword().send_keys(getttdata["userpassword"])
        register.confirmpassword().send_keys("confirmpassword")
        register.checkbox().click()
        register.login().click()

    @pytest.fixture(params= testpagedata.test_register_data)
    def getttdata(self,request):
        return request.param

