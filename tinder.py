import pyautogui
import time
cd = 2 
repeticiones = 20
click = 0
while click < repeticiones:
    time.sleep(2)
    pyautogui.click(1220, 845)
    
    print('Total de clicks:', click+1)
    print('restantes:', repeticiones - click)
    click +=1

