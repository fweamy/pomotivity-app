from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProdTrack")

        self.button = QPushButton("Press")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)

        self.setCentralWidget(self.button)

    def button_clicked(self):
        print("Clicked. Disabling now.")
        self.button.setEnabled(False)

        self.setWindowTitle("New Window")


app = QApplication([])

window = MainWindow()
window.show()

app.exec()