from selenium.webdriver.common.by import By


class Confirmpage():

    def __init__(self,driver):
        self.driver= driver

    email = (By.XPATH, "//form/div[1]/input")
    password = (By.CSS_SELECTOR, "form div:nth-child(2) input")
    confirmpassword = (By.CSS_SELECTOR, "#confirmPassword")
    newpassword = (By.XPATH, "//button[text()='Save New Password']")


    def emailpage(self):
        return self.driver.find_element(*Confirmpage.email)

    def passwordpage(self):
        return self.driver.find_element(*Confirmpage.password)

    def pageconfirmpassword(self):
        return self.driver.find_element(*Confirmpage.confirmpassword)

    def pagenewpassword(self):
        return self.driver.find_element(*Confirmpage.newpassword)










