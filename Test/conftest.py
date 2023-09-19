import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("C:\\mybrowserdriver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/client")
    driver.maximize_window()
    request.cls.driver=driver
    yield driver
    driver.quit()
