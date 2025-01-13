# Lets make a productivity app!
import csv
import os
import re
import sys
import time
import sqlite3

class TodoList():
    def __init__(self, db_connection):
        self.con = db_connection
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.check = self.cur.execute(
            """
            SELECT name 
            FROM sqlite_master 
            WHERE type='table' 
            AND name='todolist';
            """
        ).fetchall()

        if self.check == []:
            self.cur.execute(
                """CREATE TABLE todolist
                (
                    ID INTEGER PRIMARY KEY,
                    TaskName VARCHAR(255) NOT NULL,
                    TaskStatus INT NOT NULL
                );"""
            )
        else:
            print('Table found!')

    def getTdlist(self):
        self.tdlist = self.cur.execute(
            """
            SELECT * 
            FROM todolist;
            """
        ).fetchall()
        
        self.tdlist = [{k: task[k] for k in task.keys()} for task in self.tdlist]
        return self.tdlist

    def show_list(self):
        input(f"{self}\nPress ENTER to continue")

    def add_task(self, taskname):
        command = f"""
                    INSERT INTO todolist (TaskName, TaskStatus)
                    VALUES ('{taskname}', 0); 
                    """
        self.cur.execute(command)

        self.con.commit()

    def remove_task(self, tasknum):
        command = f"""
                    DELETE FROM todolist
                    WHERE ID = {tasknum} 
                    """
        self.cur.execute(command)
        
        self.con.commit()
        

    def update_task(self, tasknum):
        command = f"""
                    SELECT TaskStatus FROM todolist
                    WHERE ID = {tasknum} 
                    """
        self.cur.execute(command)
        status = self.cur.fetchone() 
        # Potential bug: status is a list/status is not an int

        status = 1 if status == 0 else 1
        command = f"""
                    UPDATE todolist
                    SET TaskStatus = {status}
                    WHERE ID = {tasknum}
                    """
        
        self.cur.execute(command)

        self.con.commit()

    def get_task(self, tasknum):
        pass

    def save_list(self):
        self.con.commit()
        self.con.close()


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

