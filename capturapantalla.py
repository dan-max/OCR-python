import cv2
import numpy as np
import pyautogui

def capturain(event, x, y, flags, param):
    if event== cv2.EVENT_LBUTTONDOWN:
        coord1=pyautogui.position() 
        print("coordenada 1" + coord1)

        return coord1
def capturafin(event, x, y, flags, param):
    if event== cv2.EVENT_LBUTTONUP:
        coord2=pyautogui.position()
        print("coordenada 2" + coord2)

        return coord2
while(1):
    resolucion = pyautogui.size()  # Esto obtiene las dimensiones de la pantalla
    ancho, alto = resolucion  # Esto desempaqueta el ancho y alto en dos variables separadas
    cv2.namedWindow('image')
    regCaptura1=cv2.setMouseCallback("image", capturain)
    regCaptura2=cv2.setMouseCallback("image", capturafin)

    if cv2.waitKey(20) & 0xFF == 27:
        break
    cv2.destroyAllWindows()

#while True:
    
# Captura la pantalla y convierte la imagen en un arreglo numpy

   # img = pyautogui.screenshot(region=(regCaptura1, regCaptura2, resolucion))

    #frame = np.array(img)
# Convierte el color de BGR a RGB
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #res= cv2.imwrite('captura.png', frame)
# Muestra el frame en una ventana (opcional)
    #cv2.imshow('Captura de pantalla', frame)
