import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import pynput
import pyautogui
import cv2
import easyocr

coord = []
def on_click(x, y, button, pressed):
    if pressed:
        print('Pressed at {0}, {1}'.format(x, y))
        coord.append(x)
        coord.append(y)
    else:
        print('Released at {0}, {1}'.format(x, y))
        coord.append(x)
        coord.append(y)
        
    if len(coord) >= 4:  # Verificar si hay suficientes coordenadas
        # Detener el listener
        return False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        with pynput.mouse.Listener(on_click=on_click) as listener:
            listener.join()

        if len(coord) >= 4:  # Asegurarse de que haya suficientes coordenadas para calcular
            if coord[2] > coord[0] and coord[3] > coord[1]:
                ancho = coord[2] - coord[0]
                alto = coord[3] - coord[1]
                top = coord[0]
                back = coord[1]
                print(alto)
                print(ancho)
            elif coord[2] > coord[0] and coord[1] > coord[3]:
                ancho = coord[2] - coord[0]
                alto = coord[1] - coord[3]
                top = coord[0]
                back = coord[3]
                print(alto)
                print(ancho)
            elif coord[0] > coord[2] and coord[3] > coord[1]:
                ancho = coord[0] - coord[2]
                alto = coord[3] - coord[1]
                top = coord[2]
                back = coord[1]
                print(alto)
                print(ancho)
            elif coord[0] > coord[2] and coord[1] > coord[3]:
                ancho = coord[0] - coord[2]
                alto = coord[1] - coord[3]
                top = coord[2]
                back = coord[3]
                print(alto)
                print(ancho)

            img = pyautogui.screenshot(region=(top, back, ancho, alto))
            img.save("prueba3.png")

            image = cv2.imread("prueba3.png")
            reader = easyocr.Reader(["en"], gpu=False)
            result = reader.readtext(image, paragraph=True,  detail = 0)

            print("result: ", result)
            archivo= open("prueba.txt","w")
            archivo.write(str(result[0]))
            archivo.close()
    
        else:
            print("No se han recopilado suficientes coordenadas para calcular.")



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
