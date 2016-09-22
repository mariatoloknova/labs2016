#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    fill_cell()
    for i in range(13):
        for j in range(i):
            fill_cell()
            move_right()
        fill_cell()
        for j in range(i):
            move_left()
        move_down()


if __name__ == '__main__':
    run_tasks()