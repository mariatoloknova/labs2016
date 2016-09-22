#!/usr/bin/python3

from pyrob.api import *

def fill_sq(n):
    move_right()
    for i in range(n):
        fill_cell()
        move_right()
    move_down()
    for i in range(n):
        fill_cell()
        move_down()
    move_left()
    for i in range(n):
        fill_cell()
        move_left()
    move_up()
    for i in range(n):
        fill_cell()
        move_up()

@task(delay=0.01)
def task_9_3():
    i = 0
    move_right()
    while(wall_is_on_the_right() != True):
        i += 1
        move_right()
    while(wall_is_on_the_left() != True):
        move_left()
    while i > 0:
        fill_sq(i)
        move_down()
        move_right()
        i -= 2
    while(wall_is_on_the_left() != True):
        move_left()
    while(wall_is_beneath() != True):
        move_down()



if __name__ == '__main__':
    run_tasks()