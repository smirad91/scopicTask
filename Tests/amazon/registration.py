from testOrganizer.TestDecorator import test, beforeEachTest, afterEachTest, print_result

from Lib.amazon import MainPage, MISC, RegisterPage
from Lib.basic import Browser, Config
from Lib.basic.Browser import go_to, close_browser

browser=None

@beforeEachTest()
def be():
    browser = Browser.createBrowser()

@afterEachTest()
def ae():
    close_browser(browser)


@test("Go to registration page")
def goToRegistration():
    go_to(browser, Config.get("amazonUrl"))
    MainPage.goToRegistration(browser)

@test("Register user")
def registerUser():
    go_to(browser, Config.get("registerUrl"))
    randomUserCredentials = MISC.generateRandomUser()
    RegisterPage.registerUser(randomUserCredentials["username"], randomUserCredentials["email"], randomUserCredentials["password"])
    MISC.deleteUser(browser, randomUserCredentials["username"])


@test("Register already existing name")
def existingName():
    username = Config.get("user")["username"]


    go_to(browser, Config.get("registerUrl"))
    RegisterPage.registerUser(browser, username, "randommail@gmail.com", "dfdfdfdfd")
    RegisterPage.checkAlertPresent()

@test("Register already existing email")
def existingEmail():
    go_to(browser, Config.get("registerUrl"))
    RegisterPage.registerUser(browser, "randomusername", "randommail@gmail.com", "dfdfdfdfd")
    RegisterPage.checkAlertPresent()

@test("Register password less than 6 char")
def passwordIncorect():
    go_to(browser, Config.get("registerUrl"))
    RegisterPage.registerUser(browser, "randomusername", "randommail@gmail.com", "dfd")
    RegisterPage.checkAlertPresent()

@test("Register reenter password wrong")
def reenterWrongPassword():
    go_to(browser, Config.get("registerUrl"))
    RegisterPage.setName(browser, "randomusername")
    RegisterPage.setEmail(browser, "randomusername@gmail.com")
    RegisterPage.setPassword(browser, "randompass")
    RegisterPage.setRePassword(browser, "randompassK")
    RegisterPage.clickRegister(browser)
    RegisterPage.checkAlertPresent()











print_result()