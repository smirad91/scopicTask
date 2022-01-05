from selenium.webdriver.common.by import By


def inpName(browser):
    return browser.find_element(By.ID, "ap_customer_name")

def inpEmail(browser):
    return browser.find_element(By.ID, "ap_email")

def inpPassword(browser):
    return browser.find_element(By.ID, "ap_password")

def inpRePassword(browser):
    return browser.find_element(By.ID, "ap_password_check")

def btnCreateAccount(browser):
    return browser.find_element(By.ID, "continue")



def setName(browser,name):
    inpName(browser).send_keys(name)

def setEmail(browser,email):
    inpEmail(browser).send_keys(email)

def setPassword(browser,password):
    inpPassword(browser).send_keys(password)

def setRePassword(browser,password):
    inpRePassword(browser).send_keys(password)

def clickRegister(browser):
    btnCreateAccount(browser).click()

def registerUser(browser, name, email, password):
    setName(browser, name)
    setEmail(browser, email)
    setPassword(browser, password)
    setRePassword(browser, password)
    clickRegister(browser)

def checkAlertPresent():
    raise Exception("ALert is not present")