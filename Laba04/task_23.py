#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    while(wall_is_on_the_right() != True):
        move_right()
        if (wall_is_above() != True):
            while (wall_is_above() != True):
                move_up()
                fill_cell()
            while(wall_is_beneath() != True):
                move_down()
    while(wall_is_above() or wall_is_beneath()):
        move_left()


if __name__ == '__main__':
    run_tasks()