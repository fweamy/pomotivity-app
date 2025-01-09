# Lets make a productivity app!
import csv
import os
import re
import sys
import time

class TodoList():
    def __init__(self, csvfile):
        self.file = csvfile
        self.file.seek(0)
        self.tdlist = list(csv.DictReader(self.file))
        self.file.truncate(0)
        self.writer = csv.DictWriter(self.file, fieldnames=["name", "status"])

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

def countdown(min):
    SEC_PER_MIN = 60
    if min < 1:
        raise ValueError("Value must be positive integer")
    for i in reversed(range(min)):
        for j in reversed(range(SEC_PER_MIN)):
            yield f"{i:02d}: {j:02d}"


def timer(timer_name="", task_name="", t=1):
    for s in countdown(t):
        os.system("clear")
        print(
            f'''
    {timer_name.upper()} - {task_name}
    {s}
            '''
        )
        time.sleep(1)

