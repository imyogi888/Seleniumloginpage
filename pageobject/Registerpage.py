from selenium.webdriver.common.by import By


class registerpage:

    def __init__(self,driver):
        self.driver= driver


    reglink= (By.LINK_TEXT, "Register")
    firname= (By.ID, "firstName")
    lasname= (By.ID, "lastName")
    emaiid= (By.ID, "userEmail")
    mobnumber= (By.ID, "userMobile")
    drop= (By.XPATH, "//div/div/select")
    gend = (By.XPATH, "//input[@value='Male']")
    userpass= (By.ID, "userPassword")
    confpass= (By.ID, "confirmPassword")
    check= (By.XPATH, "//input[@type='checkbox']")
    loginm= (By.ID, "login")




    def registerlink(self):
        return self.driver.find_element(*registerpage.reglink)

    def firstname(self):
        return self.driver.find_element(*registerpage.firname)

    def lastname(self):
        return self.driver.find_element(*registerpage.lasname)

    def emailid(self):
        return self.driver.find_element(*registerpage.emaiid)

    def mobilenumber(self):
        return self.driver.find_element(*registerpage.mobnumber)

    def dropdown(self):
        return self.driver.find_element(*registerpage.drop)

    def gender(self):
        return self.driver.find_element(*registerpage.gend)

    def userpassword(self):
        return self.driver.find_element(*registerpage.userpass)

    def confirmpassword(self):
        return self.driver.find_element(*registerpage.confpass)

    def checkbox(self):
        return self.driver.find_element(*registerpage.check)

    def login(self):
        return self.driver.find_element(*registerpage.loginm)


