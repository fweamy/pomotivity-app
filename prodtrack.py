import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QColor, QPalette
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QLabel, QTextEdit, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProdTrack")

        layout = QHBoxLayout()
        layout.addWidget(Color("red"))        
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        widget = QWidget()
        widget.setLayout(layout)
    
        self.setCentralWidget(widget)


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()