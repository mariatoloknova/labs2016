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

def plus_line():
    plus()
    while(wall_is_on_the_right() != True):
        move_right(2)
        plus()

@task
def task_2_2():
    move_down(2)
    plus_line()
    move_left(2)
    move_up()


if __name__ == '__main__':
    run_tasks()