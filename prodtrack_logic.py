# Lets make a productivity app!
import csv
import os
import re
import sys
import time


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python project.py file.csv")
    match = re.search(r"(\w+\.csv)", sys.argv[1])
    if not match:
        sys.exit("Invalid filename")
    filename = match.group(0)

    # READING (r) + not truncating/creating file if not exist (a/a+ only)
    file = open(filename, "a+")

    user_list = TodoList(file)
    user_timer = PomoTimer()

    # Main Menu
    while True:
        os.system("clear")
        user = input(menu())

        # To-do List Menu
        if user == "1":
            while True:
                os.system("clear")

                user = input(menu_td())
                match user:
                    case "1":
                        pass
                    case "2":
                        taskname = input("Task name: ")
                        user_list.add_task(taskname)
                    case "3":
                        tasknum = int(input(f"{user_list}\nTask number: "))
                        user_list.remove_task(tasknum)
                    case "4":
                        tasknum = int(input(f"{user_list}\nTask number: "))
                        user_list.update_task(tasknum)
                    case "b":
                        break
                    case _:
                        pass

                if user in ["1", "2", "3", "4"]:
                    os.system("clear")
                    user_list.show_list()

        # Pomodoro Timer Menu
        elif user == "2":
            while True:
                os.system("clear")

                user = input(menu_pomo())
                match user:
                    case "1":
                        user_timer.cycle()
                        user_timer.current_task = ""
                    case "2":
                        user_timer.current_task = user_list.get_task(
                            input(f"{user_list}\nTask number: "))
                    case "3":
                        input(f"Current Task: {user_timer.current_task}")
                    case "b":
                        break
                    case _:
                        print("Invalid input.")

        elif user == "b":
            user_list.save_list()
            file.close()
            sys.exit("Thank you for using the program.")


# CLASSES
# =============================
class TodoList():
    def __init__(self, csvfile):
        self.file = csvfile
        self.file.seek(0)
        self.tdlist = list(csv.DictReader(self.file))
        self.file.truncate(0)
        self.writer = csv.DictWriter(self.file, fieldnames=["name", "status"])

    def __str__(self):
        printlist = ""
        for i, task in enumerate(self.tdlist):
            name = task["name"]
            match task["status"]:
                case '0':
                    status = "☐"
                case '1':
                    status = "☒"
                case _:
                    status = "???"
            printlist += f"{i + 1}. {status} {name}\n"
        return printlist

    def show_list(self):
        input(f"{self}\nPress ENTER to continue")

    def add_task(self, taskname):
        task = {"name": taskname, "status": '0'}
        self.tdlist.append(task)

    def remove_task(self, tasknum):
        index = tasknum - 1
        self.tdlist.pop(index)

    def update_task(self, tasknum):
        index = tasknum - 1
        status = self.tdlist[index]["status"]
        if status == '0':
            self.tdlist[index]["status"] = '1'
        else:
            self.tdlist[index]["status"] = '0'

    def get_task(self, tasknum):
        index = int(tasknum) - 1
        return self.tdlist[index]["name"]

    def save_list(self):
        self.writer.writeheader()
        for task in self.tdlist:
            self.writer.writerow(task)


class Duration(object):
    def __init__(self, t):
        self._duration = t

    def __get__(self, instance, owner):
        return self._duration

    def __set__(self, instance, t):
        if t <= 0:
            raise TypeError("Time must be a positive number")
        self._duration = t


class PomoTimer():
    pomotime = Duration(1)
    sbreaktime = Duration(1)
    lbreaktime = Duration(1)

    def __init__(self, pomotime=25, sbreaktime=5, lbreaktime=15, task=""):
        self.pomotime = pomotime
        self.sbreaktime = sbreaktime
        self.lbreaktime = lbreaktime
        self.current_task = task

    def pomodoro(self):
        timer(timer_name="pomodoro", task_name=self.current_task, t=self.pomotime)

    def sbreak(self):
        timer(timer_name="short break", task_name=self.current_task, t=self.sbreaktime)

    def lbreak(self):
        timer(timer_name="long break", task_name=self.current_task, t=self.lbreaktime)

    def cycle(self, pomo_till_break=2):
        for _ in range(pomo_till_break):
            self.pomodoro()
            self.sbreak()
        self.lbreak()


# FUNCTIONS
# =============================
def menu():
    return (
        '''
        🌱 WELCOME TO BUDDY! 🌱
        ============================
        Choose an option. Enter b to exit.
        1. To-do List
        2. Pomodoro Timer

        Answer
        '''
    )


def menu_td():
    return (
        '''
        🌱 TO-DO LIST
        ============================
        Choose an option. Enter b to go back.
        1. View list
        2. Add task
        3. Remove task
        4. Update task's status

        Answer
        '''
    )


def menu_pomo():
    return (
        '''
        🌱 POMODORO TIMER
        ============================
        Choose an option. Enter b to go back.
        1. Start timer
        2. Set task
        3. View current task

        Answer
        '''
    )


def countdown(min):
    SEC_PER_MIN = 60
    if min < 1:
        raise ValueError("Value must be positive integer")
    for i in reversed(range(min)):
        for j in reversed(range(SEC_PER_MIN)):
            yield f"{i:02d}: {j:02d}"


def timer(timer_name="", task_name="", t=1):
    input(f"Press ENTER to start {timer_name}")
    for s in countdown(t):
        os.system("clear")
        print(
            f'''
    {timer_name.upper()} - {task_name}
    {s}
            '''
        )
        time.sleep(1)


if __name__ == "__main__":
    main()
