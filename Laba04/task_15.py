#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if (wall_is_above() and wall_is_on_the_left()):
        while(wall_is_on_the_right() != True):
            move_right()
        while(wall_is_beneath() != True):
            move_down()
    elif (wall_is_above() and wall_is_on_the_right()):
        while(wall_is_on_the_left() != True):
            move_left()
        while(wall_is_beneath() != True):
            move_down()
    elif (wall_is_beneath() and wall_is_on_the_left()):
        while(wall_is_on_the_right() != True):
            move_right()
        while(wall_is_above() != True):
            move_up()
    elif (wall_is_beneath() and wall_is_on_the_right()):
        while(wall_is_on_the_left() != True):
            move_left()
        while(wall_is_above() != True):
            move_up()

if __name__ == '__main__':
    run_tasks()