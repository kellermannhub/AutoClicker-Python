from threading import Thread
import pyautogui
from utils.paths import set_parent_directory
from vision.manager import click_cookie
from vision.manager import click_upgrade
from browser.notifier import notify


def setup():
    pyautogui.PAUSE = 0
    set_parent_directory(__file__)


def start():
    Thread(target=notify).start()
    Thread(target=click_cookie).start()
    Thread(target=click_upgrade).start()


if __name__ == "__main__":
    setup()
    start()

