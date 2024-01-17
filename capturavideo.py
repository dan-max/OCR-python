import cv2 # OpenCV
import pyautogui
import numpy as np
codec = cv2.VideoWriter_fourcc(*"MJPG")
resolucion=pyautogui.size()
out = cv2.VideoWriter("Graba.avi", codec , 20, (resolucion)) 
cv2.namedWindow("Grabando", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Grabando", resolucion)
while True:
    img = pyautogui.screenshot() # tomamos un pantallazo
    frame = np.array(img) # convertimos la imagen a un arreglo de numeros
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convertimos la imagen BGR a RGB
    out.write(frame) # adjuntamos al archivo de video
    cv2.imshow('Graban', frame) # mostramos el cuadro que acabamos de grabar
    if cv2.waitKey(33) == ord('q'): # si el usuario presiona q paramos de grabar.
        break

out.release() # cerrar el archivo de video
cv2.destroyAllWindows() # cerrar la ventana
