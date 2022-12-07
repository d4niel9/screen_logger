import pyautogui
import time


def main():
    try:
        cont = 0
        while True:
            cont += 1
            screenshot = pyautogui.screenshot()
            screenshot.save(f".\output\screen_{cont}.jpg")
            time.sleep(2) # define timeout for screenshot
    except KeyboardInterrupt as err:
        print("stop")


if __name__ == "__main__":
    main()
