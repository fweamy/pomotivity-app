import sys

from logic import *
from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtGui import QAction, QColor, QPalette
from PyQt6.QtWidgets import *

SECS_PER_MIN = 60
timerText = "00:00"
pomoTimer = PomoTimer()
todoList = TodoList()

class taskHolder(QHBoxLayout):
    def __init__ (self, task):
        super().__init__()
        self.taskName = QLabel(task["taskName"])
        self.taskStatus = QCheckBox()
        self.taskStatus.setChecked(task["taskStatus"])
        self.addWidget(self.taskName)
        self.addWidget(self.taskStatus)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Productivity Tracker")
        
        # Creates main layout holder
        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        # Creates layouts
        self.mainLayout = QHBoxLayout()
        self.timerLayout = QVBoxLayout()
        self.listLayout = QVBoxLayout()

        # Sets main layout and adds sub-layouts
        self.widget.setLayout(self.mainLayout)
        self.mainLayout.addLayout(self.timerLayout)
        self.mainLayout.addLayout(self.listLayout)

        # Creates timer display
        self.timerDisplay = QLabel(timerText)
        self.timerLayout.addWidget(self.timerDisplay)

        # Creates timer
        self.timerCountdown = QTimer()
        self.timerCountdown.timeout.connect(self.updateCountdown)
        self.timeRemaining = 0

        # Creates start button
        self.startTimerButton = QPushButton("Start")
        self.timerLayout.addWidget(self.startTimerButton) 
        self.startTimerButton.clicked.connect(self.startCountdown)

        # Creates to-do list
        tasks = [
            {
                "taskName" : "say Hi",
                "taskStatus" : True
             },
            {
                "taskName" : "say Bye",
                "taskStatus" : False
             }
        ]
        
        for task in tasks:
            taskLayout = taskHolder(task)
            self.listLayout.addLayout(taskLayout)


    # Starts countdown
    def startCountdown(self):
        self.timeRemaining = 1 * SECS_PER_MIN
        self.updateCountdown()
        self.timerCountdown.start(1000)

    # Updates timer display
    def updateCountdown(self):
        if self.timeRemaining > 0:
            mins = self.timeRemaining // SECS_PER_MIN
            secs = self.timeRemaining - mins * SECS_PER_MIN
            self.timerDisplay.setText(f"{mins:02d}:{secs:02d}")
        else:
            self.timerDisplay.setText("Time's up")
        self.timeRemaining -= 1

        



        

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