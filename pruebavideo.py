import cv2
import numpy as np
import pyautogui

# Configuración para la captura de pantalla
screen_size = (1920, 1080)  # Cambia esto al tamaño de tu pantalla
output_file = 'captura_pantalla.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_file, fourcc, 20.0, screen_size)

try:
    while True:
        # Captura la pantalla y convierte la imagen en un arreglo numpy
        img = pyautogui.screenshot()
        frame = np.array(img)

        # Convierte el color de BGR a RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Escribe el frame en el archivo de salida
        out.write(frame)

        # Muestra el frame en una ventana (opcional)
        cv2.imshow('Captura de pantalla', frame)

        # Sale del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) == ord('q'):
            break

except KeyboardInterrupt:
    pass

# Libera recursos y cierra la ventana
out.release()
cv2.destroyAllWindows()
