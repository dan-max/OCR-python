import cv2
from pynput.mouse import Listener, Button, Controller
import pyautogui
coord=[]
count=0
def on_click(x, y, button, pressed):
    if pressed and button==Button.left:
        coord.append(x)
        coord.append(y)
        print(coord)
        print(f"Clic {button} en ({x}, {y})")
        count+=count
        

# Inicializa el controlador del ratón
mouse_controller = Controller()

pyautogui.screenshot(region=())


with Listener(on_click=on_click) as listener:
        listener.join()
