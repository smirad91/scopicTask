from selenium.webdriver.common.by import By

from Lib.amazon import LoginPage, RegisterPage
from Lib.basic.Wait import wait_until


def btnSignIn(browser):
    return browser.find_element(By.XPATH, "//span[contains(text(),'Sign in')]")

def btnRegister(browser):
    return browser.find_element(By.XPATH, "//span[contains(text(),'Start here.')]")

def txtLoggedUser(browser):
    return browser.find_elements(By.CSS_SELECTOR, "span[class='nav-line-1 nav-progressive-content']")[1].text


def goToLogin(browser):
    btnSignIn(browser).click()
    wait_until(lambda: LoginPage.inpEmail(browser), timeout=5)

def goToRegistration(browser):
    btnRegister(browser).click()
    wait_until(lambda: RegisterPage.inpName(browser), timeout=5)


def checkLoggedUser(browser, expectedUser):
    loggedUser = txtLoggedUser(browser)
    if not expectedUser in loggedUser:
        raise Exception("User not as expected. Expected {0}, actual: {1}".format(expectedUser, loggedUser))