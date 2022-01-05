from selenium.webdriver.common.by import By

from Lib.basic.Wait import wait_until


def inpEmail(browser):
    return browser.find_element(By.ID, "ap_email")

def btnContinue(browser):
    return browser.find_element(By.ID, "continue")

def inpPassword(browser):
    return browser.find_element(By.ID, "ap_password")

def btnSignIn(browser):
    return browser.find_element(By.ID, "signInSubmit")

def txtAlert(browser):
    return browser.find_element(By.XPATH, "//h4[contains('There was a problem')]")



def setUsername(browser, username):
    inpEmail(browser).send_text(username)
    btnContinue(browser).click()

def setPassword(browser, password):
    inpPassword(browser).send_text(password)
    btnSignIn(browser).click()

def checkAlertPresent():
    raise Exception("ALert is not present")
