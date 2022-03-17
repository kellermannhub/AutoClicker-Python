import time
from game.info import cookies_info
from game.info import xpath_items


def notify():
    while True:
        cookies, per_second = cookies_info()

        print(f"You have: {cookies} cookies.")
        print(f"You do {per_second} cookies per second.")

        upgrades = {"cursor": 2, "grandma": 3, "farm": 4}

        cursors = xpath_items(upgrades["cursor"])
        farms = xpath_items(upgrades["grandma"])
        grandmas = xpath_items(upgrades["farm"])

        print(f"You have {cursors} cursors.")
        print(f"You have {farms} farms.")
        print(f"You have {grandmas} grandmas.")
        print("="*50)
        time.sleep(4)
