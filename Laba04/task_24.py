#!/usr/bin/python3

from pyrob.api import *

def plus():
    fill_cell()
    move_right()
    fill_cell()
    move_up()
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    move_right()
    fill_cell()

@task
def task_2_1():
    move_down(2)
    move_right()
    plus()
    move_left(2)
    move_up()


if __name__ == '__main__':
    run_tasks()