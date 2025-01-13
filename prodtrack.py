import sys

from logic import *
from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtGui import QAction, QColor, QPalette
from PyQt6.QtWidgets import *
import sqlite3

SECS_PER_MIN = 60
timerText = "00:00"
if len(sys.argv) != 2:
    sys.exit("Usage: python project.py file.csv")
match = re.search(r"(\w+\.db)", sys.argv[1])
if not match:
    sys.exit("Invalid database")
dbname = match.group(0)

# READING (r) + not truncating/creating file if not exist (a/a+ only)
connection = sqlite3.connect(dbname)
pomoTimer = PomoTimer()
todoList = TodoList(connection)


class taskHolder(QHBoxLayout):
    def __init__ (self, task):
        super().__init__()
        self.taskName = QLabel(task["TaskName"])
        self.taskStatus = QCheckBox()
        self.taskStatus.setChecked(task["TaskStatus"])
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
        mainLayout = QHBoxLayout()
        timerLayout = QVBoxLayout()
        listLayout = QVBoxLayout()

        # Sets main layout and adds sub-layouts
        self.widget.setLayout(mainLayout)
        mainLayout.addLayout(timerLayout)
        mainLayout.addLayout(listLayout)

        # Displays timer
        self.timerDisplay = QLabel(timerText)
        timerLayout.addWidget(self.timerDisplay)

        # Creates timer
        self.timerCountdown = QTimer()
        self.timerCountdown.timeout.connect(self.updateCountdown)
        self.timeRemaining = 0

        # Displays start button
        self.startTimerButton = QPushButton("Start")
        timerLayout.addWidget(self.startTimerButton) 
        self.startTimerButton.clicked.connect(self.startCountdown)

        # Displays to-do list
        for task in todoList.getTdlist():
            taskLayout = taskHolder(task)
            listLayout.addLayout(taskLayout)

        addTaskButton = QPushButton("+")
        addTaskButton.clicked.connect(self.showAddTaskWindow)
        listLayout.addWidget(addTaskButton)

    def displayList(self):
        pass

    def showAddTaskWindow(self):
        window = addTaskWindow()
        window.exec()

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

class addTaskWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Task")

        layout = QVBoxLayout()

        # Creates and displays form
        self.taskNameLineEdit = QLineEdit()
        layout.addWidget(self.taskNameLineEdit)

        # Creates and displays button boxes
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(self.buttonBox)
 
        # Adds action when form is accepted/rejectted
        self.buttonBox.accepted.connect(self.addTask)
        self.buttonBox.rejected.connect(self.reject)  

        self.setLayout(layout)

    def addTask(self):
        newTask = self.taskNameLineEdit.text()

        self.close() 

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