from testOrganizer.TestDecorator import test, beforeEachTest, afterEachTest, print_result

from Lib.amazon import MainPage, LoginPage
from Lib.basic import Browser, Config
from Lib.basic.Browser import go_to, close_browser

browser=None

@beforeEachTest()
def be():
    global browser
    browser = Browser.createBrowser()

@afterEachTest()
def ae():
    global browser
    close_browser(browser)


@test("Go to login page")
def goToLogin():
    global browser
    go_to(browser, Config.get("amazonUrl"))
    MainPage.goToLogin(browser)

@test("Login with wrong username")
def wrongUsername():
    global browser
    go_to(browser, Config.get("loginUrl"))
    LoginPage.setUsername(browser, "jkljlkjlkjl")
    LoginPage.checkAlertPresent()

@test("Login with wrong password")
def wrongPassword():
    global browser
    go_to(browser, Config.get("loginUrl"))
    LoginPage.setUsername(browser, Config.get("user")["username"])
    LoginPage.setPassword(browser, "dfsdfdsfdsfdsf")
    LoginPage.checkAlertPresent()

@test("Login with empty username")
def emptyUsername():
    global browser
    go_to(browser, Config.get("loginUrl"))
    LoginPage.setUsername(browser, "")
    LoginPage.checkAlertPresent()

@test("Login with empty password")
def emptyPassword():
    global browser
    go_to(browser, Config.get("loginUrl"))
    LoginPage.setUsername(browser, Config.get("user")["username"])
    LoginPage.setPassword(browser, "")
    LoginPage.checkAlertPresent()

@test("Login with correct credentials")
def emptyPassword():
    username = Config.get("user")["username"]
    password = Config.get("user")["password"]

    global browser
    go_to(browser, Config.get("loginUrl"))
    LoginPage.setUsername(browser, username)
    LoginPage.setPassword(browser, password)
    MainPage.checkLoggedUser(browser, username)






print_result()