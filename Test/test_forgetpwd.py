import pytest
from selenium.webdriver.common.by import By

from Testdata.testpagedata import testpagedata
from pageobject.Confirmpage import Confirmpage
from pageobject.HomePage import homepage
from utilities.baseclass import Baseclass


class TestPassword(Baseclass):
    @pytest.fixture(params=testpagedata.test_page_data)
    def getdata(self, request):
        return request.param

    
    def test_Password(self,getdata):

        home= homepage(self.driver)
        home.forget().click()
        confirm= Confirmpage(self.driver)
        confirm.emailpage().send_keys(getdata["email"])
        confirm.passwordpage().send_keys(getdata["confirm"])
        confirm.pageconfirmpassword().send_keys(getdata["password"])
        confirm.pagenewpassword().click()

