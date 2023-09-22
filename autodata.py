import pyautogui
import time

for i in range(50):
    pyautogui.click(1699,916)
    pyautogui.typewrite("Give 50 more")
    pyautogui.press('enter')
    time.sleep(30)
