from selenium.webdriver.common.by import By

from browser.manager import get_browser


def xpath_finder(xpath):
    browser = get_browser()
    return browser.find_element(By.XPATH, xpath)

