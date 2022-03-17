from vision.locator import locate_click
from vision.loader import get_image


def click_cookie():
    while True:
        locate_click(
            get_image("cookie"),
            confidence=0.5,
            region=(130, 320, 320, 310),
            grayscale=True,
        )


def click_upgrade():
    while True:
        locate_click(get_image("upgrades"), confidence=0.9995)