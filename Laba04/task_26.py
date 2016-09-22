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

def plus_table():
    for i in range(5):
        plus_line()
        while(wall_is_on_the_left() != True):
            move_left()
        move_down()
        if (wall_is_beneath()):
            move_up(2)
        else:
            move_down(3)


@task(delay=0.02)
def task_2_4():
    move_down()
    plus_table()


if __name__ == '__main__':
    run_tasks()