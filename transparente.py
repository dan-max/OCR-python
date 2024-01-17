import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QGuiApplication, QWindow

class TransparentWindow(QWindow):
    def __init__(self):
        super().__init__()
        
        # Configurar la ventana sin bordes
        self.setFlags(Qt.WindowFlags.FramelessWindowHint)
        
        # Configurar la transparencia de la ventana
        self.setOpacity(0.7)  # Ajusta la opacidad según tus necesidades
        
        # Configurar el tamaño y la posición de la ventana
        self.setGeometry(100, 100, 400, 300)

    def exposeEvent(self, event):
        # Configurar el color de fondo transparente
        transparentColor = QColor(0, 0, 0, 0)
        painter = self.window().painter()
        painter.fillRect(event.region().boundingRect(), transparentColor)

        # Dibuja lo que desees en la ventana transparente
        painter.drawText(100, 100, "¡Ventana Transparente!")

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    window = TransparentWindow()
    window.show()
    sys.exit(app.exec())
