from browser.finder import xpath_finder


def cookies_info():
    cookies_txt = (
        (xpath_finder("/html/body/div/div[2]/div[15]/div[4]").text)
        .replace("per second : ", "")
        .replace("cookies", "")
        .replace("cookie", "")
        .split("\n")
    )  # Cutting out this so our values [0] and [1] will only
    # have len() == 1 or len() == 2.

    cookies = cookies_txt[0]

    per_second = cookies_txt[-1]

    return cookies, per_second


def xpath_items(num):
    xpath_item = f"/html/body/div/div[2]/div[19]/div[3]/div[6]/div[{num}]/div[3]/div[3]"
    item_txt = xpath_finder(xpath_item).text

    if item_txt.strip() == "":
        items = 0
    else:
        items = int(item_txt)

    return items
