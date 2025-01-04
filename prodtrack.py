import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QLabel, QTextEdit, QLineEdit, QVBoxLayout, QWidget, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProdTrack")

        self.label = QLabel("Hi")
        self.setCentralWidget(self.label)

    def contextMenuEvent(self, e):
        context = QMenu(self)
        act1 = QAction("test 1", self)
        context.addAction(act1)
        act1.triggered.connect(self.hello)
        context.addAction(QAction("test 2", self))
        context.exec(e.globalPos())

    def hello(self):
        self.label.setText("Action1 clicked")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()