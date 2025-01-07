import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QColor, QPalette
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout1 = QVBoxLayout()
        layout2 = QStackedLayout()
        layout1.addLayout(layout2)

        input = QLineEdit()
        input.textChanged.connect(lambda text: self.setIndex(layout2, text))

        layout1.addWidget(input)
        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("green"))
        layout2.addWidget(Color("blue"))
        layout2.addWidget(Color("yellow"))

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

    def setIndex(self, layout: QStackedLayout, text):
        try:
            layout.setCurrentIndex(int(text)) 
        except ValueError:
            pass


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