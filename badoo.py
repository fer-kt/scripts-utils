import pyautogui    
import time
print(pyautogui.position())
repetir = 20
clicks = 0
while clicks < repetir:
    time.sleep(2)
    pyautogui.click(1267,206)
    time.sleep(2)
    pyautogui.click(700,170)
    clicks += 1
