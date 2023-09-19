import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Testdata.testpagedata import testpagedata
from pageobject.HomePage import homepage
from utilities.baseclass import Baseclass


class Testlogin(Baseclass):
    @pytest.fixture(params=testpagedata.test_login_data)
    def gettdata(self,request):
        return request.param

    def test_login(self,gettdata):
        homee= homepage(self.driver)
        homee.logemail().send_keys(gettdata["email"])
        homee.logpassword().send_keys(gettdata["password"])
        homee.submit().click()

