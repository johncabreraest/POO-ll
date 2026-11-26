import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app= QApplication(sys.argv) 
ventana= QMainWindow()
ventana.setWindowTitle("Cooperativa")
ventana.setFixedSize(400, 300)
ventana.show()
sys.exit(app.exec())
