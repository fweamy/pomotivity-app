# POMOTIVITY 🌱 - A PRODUCTIVITY APP
#### Video Demo: [POMOTIVITY 🌱 - Productivity App](https://www.youtube.com/watch?v=UOkGrrFft9E)
#### Description:
Pomotivity is a 2-in-1 productivity app where you can manage tasks with a to-do list and stay focused with a Pomodoro timer.

## Content
- app.py - Handles the execution of the program, from UI and main logic to classes and functions
- requirements.txt - A text document listing required pip libraries for the program (1 as of 1/20/2025)

## Usage
To get started, run:
```
python project.py file.db
```

`file.db` is the name of an existing SQLite database file or a new database file to store your to-do list for future uses. If no file name is inputted or file name is not in a valid DB format, the app will exit after printing instructions to the terminal.

After you inputted a valid command, the main menu will boot up:
```
🌱 WELCOME TO POMOTIVITY APP! 🌱
============================
Choose an option. Enter b to exit.
1. To-do List
2. Pomodoro Timer

Answer
|
```

Choose an option by entering your answer, e.g.
```
Answer
1
```
You can also exit the program or go back to a previous menu by entering `b`. The terminal will be cleared everytime you go to another menu to keep the interface clean and simple.

### To-do List
The app allows you to view your list, add/remove tasks, and update tasks' status accordingly to your progress. Entering 1 in the main menu will lead you to the to-do list menu:
```
🌱 TO-DO LIST
============================
Choose an option. Enter b to go back.
1. View list
2. Add task
3. Remove task
4. Update task's status
```
The app will read from an existing CSV file to access your to-do list, or create a new one for you. When closing the app, the latest version of the to-do list you edited while using the app will be saved to the file. The default fieldnames for the CSV file will always be `name`, which stores the task name, and `status`, which stores the task's completion status as a str ("0" for Incomplete and "1" for Complete.)

#### View list
View your to-do list. e.g.
```
1. ☒ Task 1
2. ☐ Task 2

Press ENTER to continue
```

#### Add/Remove task
Add/Remove tasks to/from your to-do list. Removed tasks cannot be recovered.

Adding task by entering the task **name** after being prompted. Removing task by entering the task **position** after being prompted.

#### Update task's status
Toggle task's status between '0'/'1', Incomplete/Complete, ☐/☒.

Updating task by entering the task **position** after being prompted.

### Pomodoro Timer
The app allows you to start a cycle of Pomodoro timer (2 pomodoros - 1 long break) and set a task from your to-do list to work on. Entering 2 in the main menu will lead you to the Pomodoro timer menu:
```
🌱 POMODORO TIMER
============================
Choose an option. Enter b to go back.
1. Start timer
2. Set task
3. View current task
```

#### Start timer
Start the Pomodoro timer for 1 cycle. The default cycle includes:
- 25-min work
- 5-min short break
- 25-min work
- 5-min short break
- 15-min long break

After each interval ends, a message will be prompted to move on the next interval.

#### Set task
Set a task from your to-do list to focus on during the next Pomodoro cycle.

#### View current task
View the current task set to focus on. After a Pomodoro cycle ends, the current task will be reset and you have to set it again with the "Set task" option.



