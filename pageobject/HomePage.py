from selenium.webdriver.common.by import By


class homepage():

    forgetpassword = (By.LINK_TEXT, "Forgot password?")
    loginemail= (By.ID, "userEmail")
    loginpassword= (By.ID, "userPassword")
    subbutton= (By.ID, "login")


    def __init__(self,driver):
        self.driver= driver

    def forget(self):
        return self.driver.find_element(*homepage.forgetpassword)

    def logemail(self):
        return self.driver.find_element(*homepage.loginemail)

    def logpassword(self):
        return self.driver.find_element(*homepage.loginpassword)

    def submit(self):
        return self.driver.find_element(*homepage.subbutton)



