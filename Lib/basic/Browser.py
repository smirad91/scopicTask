from selenium import webdriver

def createBrowser():
    browser = webdriver.Chrome()
    return browser

def go_to(browser, url):
    browser.get(url)

def close_browser(browser):
    browser.close()