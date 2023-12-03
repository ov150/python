import pyautogui
import time

time.sleep(5)
text = 'Sorry!!!>infinite!!'

while True:
    pyautogui.typewrite(text)

    time.sleep(1)
    pyautogui.press('enter')
 
