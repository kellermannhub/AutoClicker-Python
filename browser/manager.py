import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from utils import paths


BROWSER = None

def open_browser():
    options = webdriver.ChromeOptions()

    chrome_folder = paths.PARENT_DIRECTORY

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"user-data-dir={os.path.join(chrome_folder, 'Cookie')}")
    options.add_argument("window-size=1280,800")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    )

    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.get(r"https://xenogames224.github.io/cookieclickerxeno/")

    return browser


def get_browser():
    global BROWSER

    if not BROWSER:
        BROWSER = open_browser()
    time.sleep(3)
    BROWSER.maximize_window()

    return BROWSER
