import sys 
import pyautogui
from PyQt6.QtWidgets import QApplication, QWidget
x, y = pyautogui.size()
print(x)
print(type(x))
print(y)
print(type(y))
class VentanaVacia(QWidget):
    def __init__(self): 
        super().__init__()
        self.inicializarUI()
    def inicializarUI(self):
        self.setGeometry(0,0,x,y) 
        self.setWindowTitle("Mi primera ventana")
        self.show()
if __name__== '__main__':
    app= QApplication(sys.argv)
    ventana= VentanaVacia()
    sys.exit (app.exec())
