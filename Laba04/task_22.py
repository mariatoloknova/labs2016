#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while(wall_is_beneath() != True or wall_is_on_the_left() != True):
        while(wall_is_on_the_right() != True):
            fill_cell()
            move_right()
        fill_cell()
        while(wall_is_on_the_left() != True):
            move_left()
        if(wall_is_beneath() != True):
            move_down()
    while(wall_is_on_the_right() != True):
        fill_cell()
        move_right()
    fill_cell()
    while(wall_is_on_the_left() != True):
        move_left()


if __name__ == '__main__':
    run_tasks()