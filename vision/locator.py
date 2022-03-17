import pyautogui

def locate_click(images, confidence=0.75, region=None, grayscale=False):
    if not region:
        width, height = pyautogui.size()
        region = (0, 0, width, height)

    for image in images:
        image_loc = pyautogui.locateCenterOnScreen(
            image, confidence=confidence, region=region, grayscale=grayscale,
        )

        if image_loc:
            pos_x, pos_y = image_loc
            pyautogui.click(pos_x, pos_y)
